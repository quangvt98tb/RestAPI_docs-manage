<template>
  <section>
    <b-tabs>
      <b-tab-item label="Danh sách bình luận">
        <b-table
          :data="data"
          :columns="columns"
          :paginated="isPaginated"
          :current-page.sync="currentPage"
          :per-page="perPage"
          :sort-icon="sortIcon"
          :default-sort-direction="defaultSortDirection"
          :sort-icon-size="sortIconSize"
          :pagination-simple="isPaginationSimple"
          :pagination-position="paginationPosition"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
        >
        </b-table>
      </b-tab-item>
    </b-tabs>
  </section>
</template>
<script>
import { mapState, mapActions } from "vuex";
import DocsTable from "@/components/CreateDocs/ListDocs";
export default {
  components: {
    DocsTable,
  },
  data() {
    return {
      isPaginated: true,
      currentPage: 1,
      perPage: 5,
      checkedRows: [],
      isPaginationSimple: false,
      isPaginationRounded: true,
      paginationPosition: "bottom",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",
      checkboxPosition: "left",
      defaultSortDirection: "asc",
      //
      listBlock: [],
      data: [],
      columns: [
        {
          field: "id",
          label: "ID",
          searchable: true,
        },
        {
          field: "comment",
          label: "Nội dung",

          searchable: true,
        },
        {
          field: "id_user",
          label: "ID Người dùng",
          searchable: true,
        },
        {
          field: "id_doc",
          label: "ID Tài liệu",
          searchable: true,
        },
      ],
      selected: {},
    };
  },
  async created() {
    const { isSuccess } = await this.listAllComment();
    if (isSuccess) {
      this.data = this.list_all_comment;
    } else {
      this.data = [];
    }
  },

  computed: {
    ...mapState("comment", ["list_all_comment"]),
  },
  methods: {
    ...mapActions("comment", ["listAllComment"]),
  },
};
</script>