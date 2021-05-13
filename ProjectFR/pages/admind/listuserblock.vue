<template>
  <section>
    <div class="buttons">
      <b-button type="is-info" icon-left="account-plus" @click="pickLock"
        >Mở khóa tài khoản</b-button
      >
    </div>
    <b-tabs>
      <b-tab-item label="Dánh sách tài khoản đã khóa">
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
      <!-- <b-tab-item label="Checked rows">
        <pre>{{ checkedRows }}</pre>
      </b-tab-item> -->
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
          field: "first_name",
          label: "Họ",

          searchable: true,
        },
        {
          field: "last_name",
          label: "Tên",

          searchable: true,
        },
        {
          field: "email",
          label: "Email",

          searchable: true,
        },
        {
          field: "phone",
          label: "Điện thoại",

          searchable: true,
        },
        {
          field: "live_at",
          label: "Địa chỉ",

          searchable: true,
        },
      ],
      selected: {},
    };
  },
  async created() {
    const { isSuccess } = await this.getListBlockUsers();
    if (isSuccess) {
      this.data = this.list_user_block;
    } else {
      this.data = [];
    }
  },

  computed: {
    ...mapState("user", ["list_user_block", "dataRegister", "dataUpdate"]),
  },
  methods: {
    ...mapActions("user", [
      "getListBlockUsers",
      "registerUA",
      "updateInfoUser",
    ]),

    async pickLock() {
      if (this.checkedRows.length > 0) {
        for (let i = 0; i < this.checkedRows.length; i++) {
          this.listBlock[i] = Object.assign({}, this.checkedRows[i]);
          this.listBlock[i].role_id = 1;
          await this.updateInfoUser(this.listBlock[i]);
        }
        const { isSuccess } = await this.getListBlockUsers();
        if (isSuccess) {
          this.data = this.list_user_block;
        } else {
          this.data = [];
        }
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Thành công!",
            type: "is-success",
          });
        }, 1000);
      } else {
        this.$buefy.toast.open({
          message: "Chọn user!",
          type: "is-warning",
        });
      }
    },
  },
};
</script>