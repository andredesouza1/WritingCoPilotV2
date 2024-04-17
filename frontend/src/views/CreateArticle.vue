<template>
  <div>
    <h1>Create Article</h1>
    <div>
      <input
        type="text"
        placeholder="Enter Article Title"
        id="articleTitle"
        v-model="articleTitle"
      />
      <SelectValue_
        :statekey="statekey"
        :incrementMutation="incrementMutation"
        :decrementMutation="decrementMutation"
      />
      <!-- Pass down :index so that when we emit data from ParagraphCreationBox_ we can correctly order it below for the JSON Payload sent to the API -->
      <ParagraphCreationBox_
        v-for="index in numberOfParagraphs"
        :key="index"
        :index="index"
        :articleTitle="articleTitle"
        @paragraph-values="captureData"
      />
    </div>
    <button @click="handleClick">Create Article</button>
  </div>
</template>

<script>
import SelectValue_ from "../components/SelectValue_.vue";
import ParagraphCreationBox_ from "../components/ParagraphCreationBox_.vue";
import { useStore } from "vuex";
import { computed, ref, watch } from "vue";

export default {
  components: {
    SelectValue_,
    ParagraphCreationBox_,
  },

  setup(context) {
    const store = useStore();

    //Strings to be passed to SelectValue_ component as props
    const statekey = "numberOfParagraphs";
    const incrementMutation = "incrementParagraphs";
    const decrementMutation = "decrementParagraphs";

    const numberOfParagraphs = computed(() => store.state.numberOfParagraphs);

    // DO I want to keep paragraph Topics Dict and pragraphBulletPointLists as Dicts or change to arrays?
    const paragraphTopicsDict = ref({});

    const paragraphBulletPointLists = ref({});

    const articleTitle = ref("");

    const captureData = (data) => {
      // Merge the bullet point data from the ParagraphCreationBox_ components

      paragraphTopicsDict.value[data.index] = data.paragraphTopic;

      paragraphBulletPointLists.value[data.index] = data.bullet_point_values;

      console.log("statekey:", numberOfParagraphs.value);

      console.log(
        "Paragraph Bullet Point Lists:",
        paragraphBulletPointLists.value
      );
      console.log("Paragraph Topic:", paragraphTopicsDict.value);
    };

    const processData = () => {
      // Logic to create the payload to send to the API

      const title = document.getElementById("articleTitle").value;
      const topics = Object.values(paragraphTopicsDict.value);
      const bulletPoints = Object.values(paragraphBulletPointLists.value).map(
        (paragraphBulletPointList) => {
          return Object.values(paragraphBulletPointList);
        }
      );

      // TODO: Need to write Logic to handle empty paragraph topics and bullet points

      console.log(
        "Title:",
        title,
        "Topics:",
        topics,
        "Bullet Points:",
        bulletPoints
      );

      console.log("dataProcessed");

      return {
        title,
        topics,
        bulletPoints,
      };
    };

    const handleClick = () => {
      const { title, topics, bulletPoints } = processData();
      const model = "gpt-3.5-turbo";
      const jsonData = JSON.stringify({
        title,
        topics,
        bulletPoints,
        model,
      });

      console.log("click handled");
      console.log(jsonData);

      fetch("http://127.0.0.1:8000/llm_calls/create_article", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: jsonData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Article created:", data[0]);

          store.commit("updateArticle", data[0]);
        })
        .catch((error) => {
          console.error("Error creating article:", error);
          // Handle the error here
        });
    };

    //Allow for reactivity of the articleTitle which is passed down to the <ParagraphCreationBox_> to generate ideas
    watch(articleTitle, (newValue, oldValue) => {
      console.log("Article title changed from", oldValue, "to", newValue);
    });

    return {
      numberOfParagraphs,
      statekey,
      incrementMutation,
      decrementMutation,
      articleTitle,
      captureData,
      processData,
      handleClick,
    };
  },
};
</script>

<style></style>
