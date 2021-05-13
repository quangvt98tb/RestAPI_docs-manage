<template>
  <div>
    <div v-if="error.statusCode === 404">
      <center>
        <div>
          <img src="/images/page_not_found.png" />
        </div>
      </center>
    </div>
    <div v-else>
      <center>
        <div>
          <img src="/images/something_went_wrong.png" />
        </div>
      </center>
    </div>
  </div>
</template>

<script>
export default {
  layout: "empty",
  props: {
    error: {
      type: Object,
      default: null,
    },
  },
  head() {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError;
    return {
      title,
    };
  },
  data() {
    return {
      pageNotFound: "404 Not Found",
      otherError: "An error occurred",
    };
  },
};
</script>

<style scoped>
</style>
