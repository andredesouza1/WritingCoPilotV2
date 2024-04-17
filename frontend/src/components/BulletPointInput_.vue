<template>
  <div>
    <textarea
      type="text"
      v-model="bulletPoint"
      @keyup.enter="submitInput"
    ></textarea>
  </div>
</template>

<script>
import { ref, onUpdated, watch } from "vue";
export default {
  props: ["index", "value"],
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
