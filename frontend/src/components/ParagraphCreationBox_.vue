<template>
  <div class="paragraph-box">
    <p>Paragraph Creation Box</p>
    <ParagraphTopic_ />
    <LocalSelectValue_ @button-clicked="findNumberOfBulletPoints" />
    <BulletPointInput_ v-for="index in numberOfBulletPoints" :key="index" />
    <button>Generate Ideas</button>
  </div>
</template>

<script>
import BulletPointInput_ from "./BulletPointInput_.vue";
import LocalSelectValue_ from "./LocalSelectValue_.vue";
import ParagraphTopic_ from "./ParagraphTopic_.vue";
import { ref } from "vue";

export default {
  components: {
    LocalSelectValue_,
    BulletPointInput_,
    ParagraphTopic_,
  },
  setup() {
    const numberOfBulletPoints = ref(1);

    const findNumberOfBulletPoints = (data) => {
      console.log("Number of bullet points set:", data);
      numberOfBulletPoints.value = data;
    };

    const generateIdeas = () => {
      // Logic to generate ideas based on the selected number of bullet points
    };

    return { findNumberOfBulletPoints, numberOfBulletPoints, generateIdeas };
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
