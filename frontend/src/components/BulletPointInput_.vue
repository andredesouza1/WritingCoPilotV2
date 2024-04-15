<template>
  <div>
    <input type="text" v-model="bulletPoint" @keyup.enter="submitInput" />
  </div>
</template>

<script>
import { ref, onUpdated } from "vue";
export default {
  props: ["index"],
  setup(props, context) {
    const bulletPoint = ref("");

    const submitInput = () => {
      console.log(bulletPoint.value);
    };

    onUpdated(() => {
      console.log("On Updated Bullet");
      context.emit("updateValue", {
        index: props.index,
        value: bulletPoint.value,
      });
    });

    return { bulletPoint, submitInput };
  },
};
</script>

<style scoped>
input {
  width: 300px;
  height: 30px;
  margin: 10px;
  padding: 5px;
  border: 1px solid black;
  overflow-y: scroll;
}
</style>
