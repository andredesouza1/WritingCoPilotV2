<template>
  <div>
    <h1>View Article</h1>
    <p>{{ fullArticle }}</p>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    //fullArticle is currently being set in the store in the mutation setFullArticle
    // However, in the future I may want to change this so that the article first gets saved to a database and then retrieved from the database
    return {
      fullArticle: computed(() => store.state.fullArticle),
    };
  },
};
</script>

<style>
p {
  font-size: 16px;
  line-height: 1.5;
  color: #333;
  margin-bottom: 10px;
  max-width: 70%;
  margin: 0 auto;
}
</style>
