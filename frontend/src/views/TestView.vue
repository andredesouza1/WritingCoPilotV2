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
    <div v-if="showArea" class="area">
      <button @click="toggleArea">Close</button>
    </div>
    <button @click="toggleArea">Toggle Area</button>
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
    const numberOfIter = ref(3); // Number of Inteations
    const inputFields = ref(
      Array.from({ length: numberOfIter.value }, () => "")
    ); //Value store

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

    const showArea = ref(false);

    const toggleArea = () => {
      showArea.value = !showArea.value;
    };

    return {
      numberOfIter,
      inputFields,
      showArea,
      toggleArea,
      updateInputFields,
      handleClick,
      generateIdeas,
    };
  },
};
</script>

<style>
.area {
  position: fixed;
  top: 0;
  left: 0;
  width: 50%;
  height: 80%;
  background-color: rgb(
    241,
    233,
    233,
    0.5
  ); /* Semi-transparent white background */
  z-index: 999; /* Bring the area to the front */
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
