import { computed, watch } from "vue";
import { useStore } from "vuex";

const increment_decrement_store_value = (
  key,
  incrementMutatiton,
  decrementMutation
) => {
  const store = useStore();

  const selectedValue = computed(() => store.state[key]);

  watch(selectedValue, (newValue, oldValue) => {
    console.log("State value changed from", oldValue, "to", newValue);
  });

  return {
    increment: () => store.commit(incrementMutatiton),
    decrement: () => store.commit(decrementMutation),
    selectedValue,
  };
};

export default increment_decrement_store_value;
