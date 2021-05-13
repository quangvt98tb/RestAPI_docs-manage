<template>
  <section>
    <b-table
      :data="data"
      :columns="columns"
      :paginated="isPaginated"
      :current-page.sync="currentPage"
      :per-page="perPage"
      :selected.sync="selected"
      :sort-icon="sortIcon"
      :default-sort-direction="defaultSortDirection"
      :sort-icon-size="sortIconSize"
      :pagination-simple="isPaginationSimple"
      :pagination-position="paginationPosition"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
      @click="$emit('pick')"
    >
    </b-table>
  </section>
</template>

<script>
export default {
  props: {
    data: {
      type: Array,
    },
    selected: {
      type: Object,
    },
    columns: {
      type: Array,
    },
  },
  data() {
    return {
      isPaginated: true,
      currentPage: 1,
      perPage: 5,
      defaultSortDirection: "asc",
      isPaginationSimple: false,
      isPaginationRounded: true,
      paginationPosition: "bottom",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",
    };
  },

  methods: {},
};
</script>