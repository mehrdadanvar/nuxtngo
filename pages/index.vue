<template>
  <h1>Hello from the index page</h1>
  <div class="organization">
    <div class="cart" v-for="org in orgs" :key="org">
      <h3>{{ org.name }}</h3>
      <p>{{ org.identity }}</p>
      <p>{{ org.category }}</p>
      <p><a :href="org.link">website</a></p>
      <br />
      <p>{{ org.description }}</p>
      <p>{{ org.address }}</p>
      <p>{{ org.person }}</p>
      <p>{{ org.phone }}</p>
      <p>{{ org.social.brands }}</p>
      <div v-for="x in org.social.links" :key="x">
        <p>{{ x }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  async function call_api() {
    try {
      const response = await fetch("http://localhost:8000/api/orgs");
      const organizations = await response.json();
      return organizations;
    } catch (error) {
      if (error) {
        console.log(error);
      }
    }
  }
  let data = await call_api();
  let orgs = ref(data);
</script>

<style>
  .organization {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .cart {
    display: flex;
    flex-direction: column;
    border: 1px solid grey;
    padding: 1rem;
    max-width: 30rem;
    border-radius: 1rem;
  }
</style>
