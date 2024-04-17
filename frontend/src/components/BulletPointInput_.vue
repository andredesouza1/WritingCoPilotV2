<template>
  <div>
    <textarea type="text" v-model="bulletPoint" @input="handleInput"></textarea>
  </div>
</template>

<script>
import { ref, watch } from "vue";
export default {
  props: ["index", "inputValue"],
  setup(props, context) {
    const bulletPoint = ref(props.inputValue); //value in input

    const handleInput = (event) => {
      const newValue = event.target.value;
      bulletPoint.value = newValue;
      context.emit("inputChange", newValue); // Emit input change event to propagate to parent
    };

    watch(
      () => props.inputValue,
      (newValue) => {
        bulletPoint.value = newValue;
      }
    );

    return { bulletPoint, handleInput };
  },
};
</script>

<style scoped>
textarea {
  width: 80%;
  height: 30px;
  margin: 10px;
  padding: 5px;
  border: 1px solid black;
  overflow-y: auto;
  resize: none;
}
</style>
