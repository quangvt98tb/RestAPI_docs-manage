<template>
  <div>
    <section>
      <div class="buttons">
        <b-button type="is-info" icon-left="reply" @click="restore"
          >Khôi phục</b-button
        >
        <b-button
          type="is-danger"
          icon-left="trash-can-outline"
          @click="deleteV"
          >Xóa vĩnh viễn</b-button
        >
      </div>
    </section>
    <section>
      <b-tabs>
        <b-tab-item label="Danh sách tài liệu (đã bỏ)">
          <b-table
            :data="data"
            :columns="columns"
            :paginated="isPaginated"
            :current-page.sync="currentPage"
            :per-page="perPage"
            :checked-rows.sync="checkedRows"
            checkable
            :checkbox-position="checkboxPosition"
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
        <b-tab-item label="Checked rows">
          <pre>{{ checkedRows }}</pre>
        </b-tab-item>
      </b-tabs>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      user: null,
      data: [],
      isLoading: false,
      isFullPage: true,
      checkedRows: [],
      checkboxPosition: "left",
      isPaginated: true,
      currentPage: 1,
      perPage: 6,
      defaultSortDirection: "asc",
      isPaginationSimple: false,
      isPaginationRounded: true,
      paginationPosition: "bottom",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",
      columns: [
        {
          field: "title",
          label: "Tên tài liệu",
          searchable: true,
        },
        {
          field: "category_name",
          label: "Thể loại",
          searchable: true,
        },
        {
          field: "created",
          label: "Ngày tạo",
          centered: true,
        },
        {
          field: "updated",
          label: "Ngày cập nhật",
          centered: true,
        },
      ],
    };
  },
  async created() {
    this.user = this.$auth.$storage.getUniversal("user");
    const inp = {
      id: Number(this.user.id),
    };
    const { isSuccess } = await this.getListDeleteDocsById(inp);
    if (isSuccess) {
      this.data = this.listdocsdel;
    } else {
      this.data = [];
    }
  },
  computed: {
    ...mapState("docs", ["listdocsdel", "delData", "dataRestore"]),
  },
  methods: {
    ...mapActions("docs", [
      "getListDeleteDocsById",
      "deleteDocVV",
      "restoreDocs",
    ]),
    async restore() {
      let dataid = {
        ids: [],
      };
      for (let i = 0; i < this.checkedRows.length; i++) {
        dataid.ids[i] = this.checkedRows[i].id;
      }

      const { isSuccess } = await this.restoreDocs(dataid);
      if (isSuccess) {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Khôi phục thành công!",
            type: "is-success",
          });
          this.$router.push("/docs/listdocs");
        }, 500);
      } else {
        this.$buefy.toast.open({
          message: "Có lỗi xảy ra!",
          type: "is-danger",
        });
      }
    },
    async deleteV() {
      let dataid = {
        ids: [],
      };
      for (let i = 0; i < this.checkedRows.length; i++) {
        dataid.ids[i] = this.checkedRows[i].id;
      }

      const { isSuccess } = await this.deleteDocVV(dataid);
      if (isSuccess) {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Xóa thành công!",
            type: "is-success",
          });
          this.$router.push("/docs/listdocs");
        }, 500);
      } else {
        this.$buefy.toast.open({
          message: "Có lỗi xảy ra!",
          type: "is-danger",
        });
      }
    },
  },
};
</script>