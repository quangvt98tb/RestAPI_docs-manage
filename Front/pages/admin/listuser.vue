<template>
  <section>
    <DocsTable
      :data="dataTable"
      :columns="dataColumns"
      :selected="selected"
      @updete="checkLock"
    />
  </section>
</template>
<script>
import { mapState, mapActions } from "vuex";
import DocsTable from "@/components/CreateDocs/ListDocs";
export default {
  layout: "default-admin",
  components: {
    DocsTable,
  },
  data() {
    return {
      dataTable: [],
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
    const { isSuccess } = await this.getListUsers();
    if (isSuccess) {
      this.dataTable = this.list_user_info;
      this.selected = this.dataTable[0];
    } else {
      this.dataTable = [];
    }
  },

  computed: {
    ...mapState("user", ["list_user_info", "dataRegister"]),
  },
  methods: {
    ...mapActions("user", ["getListUsers", "registerUA"]),

    checkLock() {
      console.log(this.selected);
    },
  },
};
</script>