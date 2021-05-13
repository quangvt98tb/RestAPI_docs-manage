<template>
  <section>
    <div class="buttons">
      <b-button
        type="is-info"
        icon-left="account-plus"
        @click="isCreated = !isCreated"
        >Thêm mới</b-button
      >
    </div>

    <div v-if="!isCreated">
      <b-tabs>
        <b-tab-item>
          <b-table
            :data="dataTable"
            :columns="dataColumns"
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
    </div>

    <div v-if="isCreated">
      <b-field horizontal label="Họ">
        <b-input
          type="text"
          placeholder="Tên họ"
          v-model="userData.first_name"
          required
        ></b-input>
      </b-field>
      <b-field horizontal label="Tên">
        <b-input
          type="text"
          placeholder="Tên"
          v-model="userData.last_name"
          required
        ></b-input>
      </b-field>
      <b-field horizontal label="Mật khẩu">
        <b-input type="password" v-model="userData.password" required></b-input>
      </b-field>
      <b-field horizontal label="Email">
        <b-input
          type="email"
          placeholder="Email"
          v-model="userData.email"
          required
        ></b-input>
      </b-field>
      <b-field horizontal label="Số điện thoại">
        <b-input
          v-model="userData.phone"
          type="text"
          placeholder="Số điện thoại"
          required
        ></b-input>
      </b-field>
      <b-field horizontal label="Đại chỉ">
        <b-input
          v-model="userData.live_at"
          type="text"
          placeholder="Địa chỉ"
          required
        ></b-input>
      </b-field>

      <br />
      <b-button @click="createUser" class="is-success" style="float: right"
        >Lưu tài khoản</b-button
      >
    </div>
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
      userData: {
        email: null,
        password: null,
        first_name: null,
        last_name: null,
        phone: null,
        live_at: null,
        role_id: 0,
      },
      isCreated: false,
      dataTable: [],
      selected: {},
      dataColumns: [
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
    const { isSuccess } = await this.getListAdmin();
    if (isSuccess) {
      this.dataTable = this.list_admin_info;
    } else {
      this.dataTable = [];
    }
  },

  computed: {
    ...mapState("user", ["list_admin_info", "dataRegister"]),
  },
  methods: {
    ...mapActions("user", ["getListAdmin", "registerUA"]),

    async createUser() {
      const { isSuccess } = await this.registerUA(this.userData);
      if (isSuccess) {
        console.log(this.dataRegister);
        await this.getListAdmin();
        this.dataTable = this.list_admin_info;
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Thành công!",
            type: "is-success",
          });
        }, 300);
      } else {
        this.$buefy.toast.open({
          message: "Có lỗi xảy ra!",
          type: "is-danger",
        });
      }

      this.isCreated = false;
    },
  },
};
</script>