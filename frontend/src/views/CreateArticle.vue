<template>
  <div>
    <h1>Create Article</h1>
    <div>
      <input type="text" placeholder="Enter Article Title" />
      <SelectValue_
        :statekey="statekey"
        :incrementMutation="incrementMutation"
        :decrementMutation="decrementMutation"
      />
      <ParagraphCreationBox_ v-for="index in numberOfParagraphs" :key="index" />
    </div>
  </div>
</template>

<script>
import SelectValue_ from "../components/SelectValue_.vue";
import ParagraphCreationBox_ from "../components/ParagraphCreationBox_.vue";
import { useStore } from "vuex";
import { computed } from "vue";

export default {
  components: {
    SelectValue_,
    ParagraphCreationBox_,
  },

  setup() {
    const store = useStore();

    const statekey = "numberOfParagraphs";
    const incrementMutation = "incrementParagraphs";
    const decrementMutation = "decrementParagraphs";

    return {
      numberOfParagraphs: computed(() => store.state.numberOfParagraphs),
      statekey,
      incrementMutation,
      decrementMutation,
    };
  },
};
</script>

<style></style>
