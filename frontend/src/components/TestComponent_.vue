<template>
  <input type="text" :value="inputValue" @input="handleInput" />
</template>

<script>
import { ref, watch } from "vue";

export default {
  props: ["inputValue"],
  setup(props, { emit }) {
    const inputValue = ref(props.inputValue);

    const handleInput = (event) => {
      const newValue = event.target.value;
      inputValue.value = newValue;
      emit("inputChange", newValue); // Emit input change event to propagate to parent
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
