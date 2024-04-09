import { createStore } from "vuex";

const store = createStore({
  strict: true,
  state() {
    return {
      numberOfParagraphs: 1,
    };
  },
  mutations: {
    incrementParagraphs(state) {
      state.numberOfParagraphs++;
      if (state.numberOfParagraphs > 30) {
        state.numberOfParagraphs = 30;
      }
    },
    decrementParagraphs(state) {
      state.numberOfParagraphs--;
      if (state.numberOfParagraphs < 1) {
        state.numberOfParagraphs = 1;
      }
    },
  },
  actions: {},
  getters: {
    getNumberOfParagraphs: (state) => state.numberOfParagraphs,
  },
});

export default store;
