<template>
  <div>
    <input
      type="text"
      v-model="bulletPoint"
      @keyup.enter="submitInput"
      @input="updateValue"
    />
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {
    const bulletPoint = ref("");

    const submitInput = () => {
      console.log(bulletPoint.value);
    };

    const updateValue = () => {
      // Ensure the value is a number

      console.log(bulletPoint.value);
    };

    return { bulletPoint, submitInput, updateValue };
  },
};
</script>

<style></style>
