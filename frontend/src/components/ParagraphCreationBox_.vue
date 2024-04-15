<template>
  <div class="paragraph-box">
    <p>Paragraph Creation Box</p>
    <div>
      <input
        type="text"
        placeholder="Enter Paragraph Topic"
        name="p_topic"
        v-model="paragraphTopic"
      />
    </div>
    <LocalSelectValue_ @button-clicked="findNumberOfBulletPoints" />
    <BulletPointInput_
      v-for="index in numberOfBulletPoints"
      :key="index"
      :index="index"
      @update-value="trackBulletPointValue"
    />
    <button>Generate Ideas</button>
  </div>
</template>

<script>
import BulletPointInput_ from "./BulletPointInput_.vue";
import LocalSelectValue_ from "./LocalSelectValue_.vue";

import { ref, onUpdated } from "vue";

export default {
  components: {
    LocalSelectValue_,
    BulletPointInput_,
  },
  props: ["index"],
  setup(props, context) {
    const numberOfBulletPoints = ref(1);

    const bulletPointValuesDict = ref({});

    const paragraphTopic = ref("");

    const findNumberOfBulletPoints = (data) => {
      console.log("Number of bullet points set:", data);
      numberOfBulletPoints.value = data;

      // Get an array of keys from bulletPointValuesDict
      const keysToDelete = Object.keys(bulletPointValuesDict.value).filter(
        (key) => parseInt(key) > data
      );

      // Delete the key-value pairs associated with keysToDelete
      keysToDelete.forEach((key) => {
        delete bulletPointValuesDict.value[key];
      });

      console.log("Bullet Point Values Dict:", bulletPointValuesDict.value);
    };

    const trackBulletPointValue = (data) => {
      bulletPointValuesDict.value[data.index] = data.value;

      console.log("Bullet Point Values Dict:", bulletPointValuesDict.value);

      context.emit("paragraphValues", {
        index: props.index,
        bullet_point_values: bulletPointValuesDict.value,
        paragraphTopic: paragraphTopic.value,
      });
    };

    const generateIdeas = () => {
      // Logic to generate ideas based on the selected number of bullet points
    };

    onUpdated(() => {
      context.emit("paragraphValues", {
        index: props.index,
        bullet_point_values: bulletPointValuesDict.value,
        paragraphTopic: paragraphTopic.value,
      });
    });

    return {
      numberOfBulletPoints,
      paragraphTopic,
      findNumberOfBulletPoints,
      trackBulletPointValue,
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

  min-height: 20vh;
}
</style>
