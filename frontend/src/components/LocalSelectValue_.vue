<template>
  <div class="number-selector">
    <button @click="decrement">-</button>
    <input type="text" v-model="localSelectedValue" class="selected_value" />
    <button @click="increment">+</button>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup(props, context) {
    const localSelectedValue = ref(1);

    const increment = () => {
      if (localSelectedValue.value < 50) {
        localSelectedValue.value++;
      }
      context.emit("buttonClicked", localSelectedValue.value);
    };

    const decrement = () => {
      if (localSelectedValue.value > 1) {
        localSelectedValue.value--;
      }
      context.emit("buttonClicked", localSelectedValue.value);
    };

    return { increment, decrement, localSelectedValue };
  },
};
</script>

<style scoped>
.number-selector {
  display: flex;
  flex-direction: row;
  align-items: right;
}

.number-selector button {
  padding: 5px 10px;
  cursor: pointer;
  padding: 5px;
  width: 25px;
  height: 27px;
  text-align: center;
}

input {
  width: 50px;
  text-align: center;
}

.selected_value {
  background-color: lightgrey;
  border: 1px solid black;
  padding: 5px;
  width: 20px;
  height: 15px;
}
</style>
