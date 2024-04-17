<template>
  <div>
    <nav id="navbar">
      <router-link to="/">Home</router-link>
      <router-link to="/create-article">Create Article</router-link>
      <router-link to="/view-article">View Article</router-link>
      <router-link to="/test-view">Test View</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#navbar {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: lightskyblue;
  z-index: 1000; /* Ensure the navbar stays on top */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a shadow for better visibility */
  transition: top 0.3s; /* Add smooth transition */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 20px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

h1 {
  margin-top: 100px;
}
</style>
