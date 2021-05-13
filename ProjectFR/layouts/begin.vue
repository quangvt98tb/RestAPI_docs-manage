<template>
  <div class="login-page">
    <!-- <the-nav /> -->
    <nuxt />
    <the-footer />
  </div>
</template>

<script>
import TheFooter from "@/components/TheFooter";
import TheNav from "@/components/TheNav";
export default {
  components: { TheFooter, TheNav },
  head() {
    return {
      htmlAttrs: {
        class: [
          "has-aside-left",
          "has-aside-mobile-transition",
          "has-aside-expanded",
        ],
      },
    };
  },
};
</script>

<style scoped>
.login-page {
  margin-top: 7px;
}
</style>