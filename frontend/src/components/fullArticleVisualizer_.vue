<template>
  <div>
    <div class="overlay">
      <button class="overlay-button" @click="handleClick">Close</button>
      <p>{{ fullArticle }}</p>
    </div>
    <button class="saveButton">Save and Edit Article</button>
  </div>
</template>

<script>
import { useStore } from "vuex";
export default {
  setup(props, context) {
    const store = useStore();

    const fullArticle = store.state.fullArticle;

    const handleClick = () => {
      context.emit("toggleArticle");
    };

    return {
      fullArticle,
      handleClick,
    };
  },
};
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgb(241, 233, 233);
  z-index: 999; /* Bring the area to the front */
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay-button {
  cursor: pointer;
}

.saveButton {
  position: fixed;
  bottom: 20%;
  left: 1%;
  width: 50px;
  height: 50px;
  background-color: rgb(241, 233, 233);
  z-index: 999; /* Bring the area to the front */
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: x-small;
  font-weight: bold;
  color: rgb(0, 0, 0);
  border: none;
  border: 1px solid rgb(0, 0, 0);
  outline: none;
}

.saveButton:hover {
  background-color: rgb(255, 0, 0);
  color: rgb(255, 255, 255);
}
</style>
