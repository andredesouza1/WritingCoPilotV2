<template>
  <div class="number-selector">
    <button @click="decrement">-</button>
    <input type="text" v-model="selectedValue" class="selected_value" />
    <button @click="increment">+</button>
  </div>
</template>

<script>
import increment_decrement_store_value from "../composables/increment_decrement_store_value";

export default {
  props: ["statekey", "incrementMutation", "decrementMutation"],
  setup(props) {
    const { increment, decrement, selectedValue } =
      increment_decrement_store_value(
        props.statekey,
        props.incrementMutation,
        props.decrementMutation
      );
    return { increment, decrement, selectedValue };
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
