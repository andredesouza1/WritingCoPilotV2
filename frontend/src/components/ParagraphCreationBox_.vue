<template>
  <div class="paragraph-box">
    <p>Paragraph Creation Box</p>
    <div>
      <input
        type="text"
        placeholder="Enter Paragraph Topic"
        name="p_topic"
        id="p_topic"
        v-model="paragraphTopic"
      />
    </div>
    <LocalSelectValue_ @button-clicked="findNumberOfBulletPoints" />
    <BulletPointInput_
      v-for="(inputValue, index) in bulletPointValues"
      :key="index"
      :index="index"
      :inputValue="inputValue"
      @inputChange="updateInputFields(index, $event)"
    />
    <button @click="generateIdeas">Generate Ideas</button>
  </div>
</template>

<script>
import BulletPointInput_ from "./BulletPointInput_.vue";
import LocalSelectValue_ from "./LocalSelectValue_.vue";

import { ref, onUpdated, watch } from "vue";

export default {
  components: {
    LocalSelectValue_,
    BulletPointInput_,
  },
  props: ["index", "articleTitle"],
  setup(props, context) {
    const numberOfBulletPoints = ref(1); // Number of Iterations

    const bulletPointValues = ref(
      Array.from({ length: numberOfBulletPoints.value }, () => "")
    ); //Value store

    const articleTitleName = ref(props.articleTitle);

    const paragraphTopic = ref("");

    watch(
      () => numberOfBulletPoints.value,
      (newValue, oldValue) => {
        // Update inputFields array length based on the new value of numberOfIter
        bulletPointValues.value = Array.from(
          { length: newValue },
          (_, index) => {
            return bulletPointValues.value[index] || ""; // Preserve existing values if possible
          }
        );
      }
    );

    watch(
      () => props.articleTitle,
      (newValue) => {
        articleTitleName.value = newValue;
      }
    );

    const findNumberOfBulletPoints = (data) => {
      console.log("Number of bullet points set:", data);
      numberOfBulletPoints.value = data;
    };

    // const trackBulletPointValue = (data) => {
    //   bulletPointValuesDict.value[data.index] = data.value;

    //   console.log("Bullet Point Values Dict:", bulletPointValuesDict.value);

    //   context.emit("paragraphValues", {
    //     index: props.index,
    //     bullet_point_values: bulletPointValuesDict.value,
    //     paragraphTopic: paragraphTopic.value,
    //   });
    // };

    const updateInputFields = (index, value) => {
      bulletPointValues.value[index] = value;
      console.log("Input Fields:", bulletPointValues.value);
      console.log("Number of Iterations:", numberOfBulletPoints.value);
    };

    const generateIdeas = () => {
      const articleTitle = articleTitleName.value;
      const topic = paragraphTopic.value;
      const number = numberOfBulletPoints.value;
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
          for (
            let i = 0;
            i < Math.min(numberOfBulletPoints.value, data.length);
            i++
          ) {
            console.log(i, data[i]);
            bulletPointValues.value[i] = data[i];
            console.log(bulletPointValues.value);
          }
        })
        .catch((error) => {
          console.error("Error creating article:", error);
          // Handle the error here
        });
    };

    onUpdated(() => {
      context.emit("paragraphValues", {
        index: props.index,
        bullet_point_values: bulletPointValues.value,
        paragraphTopic: paragraphTopic.value,
      });
    });

    return {
      numberOfBulletPoints,
      paragraphTopic,
      bulletPointValues,
      articleTitleName,
      findNumberOfBulletPoints,
      updateInputFields,
      generateIdeas,
    };
  },
};
</script>

<style scoped>
.paragraph-box {
  width: 80%;
  background-color: grey;
  margin: 0 auto;
}

#p_topic {
  width: 50%;
}
</style>
