<template>
  <client-only>
    <div class="app">
      <div>
        <section class="navi">
          <the-nav />
        </section>
      </div>
      <div class="columns">
        <section class="column is-one-fifth">
          <the-nav-bar />
        </section>

        <section class="column is-three-quarters container">
          <br />
          <nuxt />
        </section>
      </div>
      <the-footer />
    </div>
  </client-only>
</template>

<script>
import TheNavBar from "@/components/TheNavBar";
import TheFooter from "@/components/TheFooter";
import TheNav from "@/components/TheNav";
export default {
  components: { TheNavBar, TheFooter, TheNav },
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
.app {
  background-color: #f0f3f3;
}
.navi {
  margin-top: 7px;
}
</style>
