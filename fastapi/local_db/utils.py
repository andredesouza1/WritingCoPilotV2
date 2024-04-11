from llm_functions import call_llm
from typing import List



# Define the Paragraph class

class Paragraph:
    def __init__(self, paragraph_topic:str):
        self.paragraph_topic = paragraph_topic
        self.bullet_points = []

# Define the Node and Queue Classes to process Article Writing

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
       

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
        return current.data




#Manage Queue

def create_queue(topics:List[str],bullet_point_lists:List[List[str]]):
    """
    Process paragraph topics and bullet points and create queue in order to iterativly create the paragraphs within process_queue().

    Using the number of topics and bullet point lists as proxies for number of paragraphs to be generated.

    """

    print("Entering queue Creation")
    my_queue = Queue()
    
    for i in range(len(topics)):
        print("i", i)
        new_data = Paragraph(topics[i])
        for j in range(len(bullet_point_lists[i])):
            new_data.bullet_points.append(bullet_point_lists[i][j])

    
        my_queue.enqueue(new_data)

    return my_queue


def process_queue(my_queue, openai_api_key:str, model:str = 'gpt-3.5-turbo'):
    """
    Process queue dequeue each Paragraph to be written from the queue and passive the information to the llm.

    
    """
    
    
    
    # Define variables
    article = ""
    topic = ""
    bullet_points = ""
    bullet_points_list = []
    paragraphs = []

    # While there are items in the queue loop through and create the next Paragraph in the sequence
    
    while my_queue.count > 0:
        print("Queue Count:", my_queue.count)  # For testing purposes
        my_data = my_queue.dequeue() # Grabs data from the first item in the queue
        topic = my_data.paragraph_topic   # Saves the Paragraph topic to use when calling the llm
        print("Topic:", topic)
        bullet_points = str(my_data.bullet_points) # Saves bulletpoints as string for use in llm
        print("Bullet Points:", bullet_points)
        bullet_points_list.append(my_data.bullet_points) # Saves bullet points in a list for use in cosine similarity function later
        response = call_llm(article, topic, bullet_points, openai_api_key, model) # Calls the llm and saves response
        paragraphs.append(response) # Appends the reponse to the paragraph list 
        article += "\n\n" + response # Adds the new Paragraph each time the llm is called to the current article
        print(article)

    # Return the article, paragraphs and bullet points list for further use
    return article, paragraphs, bullet_points_list