<template>
  <section>
    <div class="buttons">
      <b-button
        type="is-info"
        icon-left="animation-outline"
        @click="addCategory"
        >Thêm mới</b-button
      >
      <b-button type="is-info" icon-left="animation-outline">Cập nhật</b-button>
      <b-button type="is-danger" icon-left="animation-outline">Xóa</b-button>
    </div>
    <DocsTable :data="dataTable" :columns="dataColumns" :selected="selected" />
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
      selected: {},
      new_catlog: {
        name_category: "",
        note: "",
      },
      dataColumns: [
        {
          field: "id",
          label: "ID",
          searchable: true,
        },
        {
          field: "name_category",
          label: "Thể loại",
          searchable: true,
        },
      ],
      selected: {},
    };
  },
  async created() {
    const { isSuccess } = await this.listCategory();
    if (isSuccess) {
      this.dataTable = this.list_category;
      this.selected = this.dataTable[0];
    } else {
      this.dataTable = [];
    }
  },

  computed: {
    ...mapState("category", [
      "list_category",
      "dataCreateCategory",
      "dataUpdateCategory",
      "dataDeleteCategory",
    ]),
  },
  methods: {
    ...mapActions("category", [
      "listCategory",
      "createCategory",
      "updateCategory",
      "deleteCategory",
    ]),

    checkLock() {
      console.log(this.selected);
    },
    async addCategory() {},

    //
  },
};
</script>