<template>
  <client-only>
    <div class="app1">
      <div>
        <section class="navi">
          <TheNavBarAdmin />
        </section>
      </div>
      <div class="columns">
        <section class="column is-one-fifth">
          <TheNavAdmin />
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
import TheNav from "@/components/TheNav";
import TheFooter from "@/components/TheFooter";
import TheNavAdmin from "@/components/Admin/TheNavAdmin";
import TheNavBarAdmin from "../components/Admin/TheNavBarAd";
export default {
  components: { TheNav, TheFooter, TheNavAdmin, TheNavBarAdmin },
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
.app1 {
  background-color: #f0f3f3;
}
.navi {
  margin-top: 7px;
}
</style>
