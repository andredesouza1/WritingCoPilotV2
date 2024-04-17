<template>
  <div>
    <h1>TestView</h1>
    <button @click="numberOfIter++">Increment</button>
    <button @click="numberOfIter--">Decrement</button>
    <TestComponent_
      v-for="(inputValue, index) in inputFields"
      :key="index"
      :inputValue="inputValue"
      @inputChange="updateInputFields(index, $event)"
    />
    <button @click="handleClick">Generate Ideas</button>
  </div>
</template>

<script>
import TestComponent_ from "../components/TestComponent_.vue";
import { ref, watch } from "vue";

export default {
  components: {
    TestComponent_,
  },
  setup() {
    const numberOfIter = ref(3);
    const inputFields = ref(
      Array.from({ length: numberOfIter.value }, () => "")
    );

    watch(
      () => numberOfIter.value,
      (newValue, oldValue) => {
        // Update inputFields array length based on the new value of numberOfIter
        inputFields.value = Array.from({ length: newValue }, (_, index) => {
          return inputFields.value[index] || ""; // Preserve existing values if possible
        });
      }
    );

    const updateInputFields = (index, value) => {
      inputFields.value[index] = value;
      console.log("Input Fields:", inputFields.value);
      console.log("Number of Iterations:", numberOfIter.value);
    };

    const handleClick = () => {
      generateIdeas();
    };

    const generateIdeas = () => {
      const articleTitle = "Countries of the World";
      const topic = "Countries in the Middle East";
      const number = numberOfIter.value;
      const model = "gpt-3.5-turbo";
      const jsonData = JSON.stringify({
        articleTitle,
        topic,
        number,
        model,
      });

      console.log(jsonData);

      fetch("http://127.0.0.1:8000/llm_calls/generate_bulletpoints", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: jsonData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("BulletPoints:", data);
          for (let i = 0; i < Math.min(numberOfIter.value, data.length); i++) {
            console.log(i, data[i]);
            inputFields.value[i] = data[i];
          }

          console.log("Input Fields:", inputFields.value);
        })
        .catch((error) => {
          console.error("Error creating article:", error);
          // Handle the error here
        });
    };

    return {
      numberOfIter,
      inputFields,
      updateInputFields,
      handleClick,
      generateIdeas,
    };
  },
};
</script>

<style></style>
