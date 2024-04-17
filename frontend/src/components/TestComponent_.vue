<template>
  <div>
    <input type="text" :value="inputValue" @input="handleInput" />
  </div>
</template>

<script>
import { ref, watch } from "vue";

export default {
  props: ["inputValue"],
  setup(props, context) {
    const inputValue = ref(props.inputValue); //Value in input

    const handleInput = (event) => {
      const newValue = event.target.value;
      inputValue.value = newValue;
      context.emit("inputChange", newValue); // Emit input change event to propagate to parent
    };

    watch(
      () => props.inputValue,
      (newValue) => {
        inputValue.value = newValue;
      }
    );

    return { inputValue, handleInput };
  },
};
</script>

<style></style>
