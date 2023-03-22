<template>
  <main class="register">
    <div class="image"></div>
    <div class="container w-1/3 border border-slate-300 rounded-lg">
      <form class="flex flex-col gap-12">
        <h1>Registeration Form</h1>
        <div class="flex flex-row gap-6">
          <div class="flex flex-row gap-4">
            <label for="">First Name</label>
            <input type="text" class="border border-slate-200" />
          </div>
          <div class="flex flex-row gap-4">
            <label for="">Last Name</label>
            <input type="text" class="border border-slate-200" />
          </div>
        </div>
        <div>
          <label for="">Email Address</label>
          <input type="text" class="border border-slate-200" />
        </div>
        <div class="input-item-icon">
          <label for="">Password</label>
          <span>
            <input :type="identifier" class="border border-slate-200" />
            <i @click.prevent="toggle">
              <img src="../assets/eye.svg" alt="" />
            </i>
          </span>
        </div>
        <div class="input-item-icon">
          <label for=""> confirm Password</label>
          <span>
            <input :type="identifier" class="border border-slate-200" />
            <i @click.prevent="toggle">
              <img src="../assets/eye.svg" alt="" />
            </i>
          </span>
        </div>
        <div class="flex flex-row gap-6">
          <button class="bg-slate-800 text-white">Create Account</button>
          <button><NuxtLink to="/Login">I have an Account</NuxtLink></button>
        </div>
      </form>
    </div>
  </main>
</template>
<script setup>
let identifier = ref("password");
function toggle() {
  if (identifier.value === "password") {
    identifier.value = "text";
  } else {
    identifier.value = "password";
  }
}
</script>
