<template>
  <div>
    <section>
      <div class="buttons">
        <b-button
          v-if="!isEdit"
          type="is-info"
          icon-left="animation-outline"
          @click="isCreated = !isCreated"
          >Thêm mới</b-button
        >
        <b-tooltip
          label="Chọn thể loại cần chỉnh sửa"
          position="is-bottom"
          v-if="!isCreated"
        >
          <b-button type="is-info" icon-left="animation-outline" @click="editC"
            >Cập nhật</b-button
          >
        </b-tooltip>
      </div>
    </section>
    <section v-if="isCreated">
      <b-field label="Tên thể loại">
        <b-input placeholder="Tên thể loại" v-model="name_c" required></b-input>
      </b-field>
      <b-field label="Ghi chú">
        <b-input placeholder="Chú thích thêm" v-model="note"></b-input>
      </b-field>
      <b-field>
        <b-button type="is-success" @click="addCategory">Lưu thêm mới</b-button>
      </b-field>
    </section>
    <section v-if="!isCreated">
      <b-tabs v-if="!isEdit">
        <b-tab-item label="Thể loại">
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
    <div v-if="isEdit">
      <section>
        <div v-for="(edit_category, index) in listEditCate" :key="index">
          <b-field label="ID thể loại">
            <b-input v-model="edit_category.id" readonly></b-input>
          </b-field>
          <b-field label="Tên thể loại">
            <b-input
              placeholder="Tên thể loại"
              v-model="edit_category.name_category"
              required
            ></b-input>
          </b-field>
          <b-field label="Ghi chú">
            <b-input
              placeholder="Chú thích thêm"
              v-model="edit_category.note"
            ></b-input>
          </b-field>
        </div>
        <br />
        <b-field>
          <div class="buttons">
            <b-button type="is-success" @click="editCate">Lưu</b-button>
            <b-button type="is-danger" @click="isEdit = false">Thoát</b-button>
          </div>
        </b-field>
      </section>
    </div>
  </div>
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
      // table
      isPaginated: true,
      currentPage: 1,
      perPage: 5,

      isPaginationSimple: false,
      isPaginationRounded: true,
      paginationPosition: "bottom",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",
      checkboxPosition: "left",
      defaultSortDirection: "asc",
      //
      isEdit: false,
      isCreated: false,
      name_c: null,
      note: null,
      data: [],
      checkedRows: [],
      new_catlog: {
        name_category: "",
        note: "",
      },
      listEditCate: [],
      columns: [
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
        {
          field: "note",
          label: "Ghi chú",
        },
      ],
    };
  },
  async created() {
    const { isSuccess } = await this.listCategory();
    if (isSuccess) {
      this.data = this.list_category;
    } else {
      this.data = [];
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
      console.log(this.selected.id);
    },
    async addCategory() {
      if (this.name_c === "") {
        this.$buefy.toast.open({
          message: "Chưa điền thông tin cần thiết!",
          type: "is-danger",
        });
      } else {
        this.new_catlog.name_category = this.name_c;
        this.new_catlog.note = this.note;
        const { isSuccess } = await this.createCategory(this.new_catlog);
        if (isSuccess) {
          await this.listCategory();
          this.data = this.list_category;
          this.$buefy.toast.open({
            message: "Thành công!",
            type: "is-success",
          });
        } else {
          this.$buefy.toast.open({
            message: "Không thành công!",
            type: "is-danger",
          });
        }
      }
      setTimeout(() => {
        this.isCreated = false;
      }, 500);
    },

    editC() {
      if (this.checkedRows.length > 0) {
        for (let i = 0; i < this.checkedRows.length; i++) {
          this.listEditCate[i] = Object.assign({}, this.checkedRows[i]);
        }
        console.log(this.listEditCate);
        setTimeout(() => {
          this.isEdit = true;
        }, 500);
      } else {
        this.$buefy.toast.open({
          message: "Chọn thể loại!",
          type: "is-warning",
        });
      }
    },

    async editCate() {
      console.log(this.listEditCate);
      try {
        for (let i = 0; i < this.listEditCate.length; i++) {
          await this.updateCategory(this.listEditCate[i]);
        }

        await this.listCategory();
        this.data = this.list_category;
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Thành công!",
            type: "is-success",
          });
          this.isEdit = false;
        }, 1000);
      } catch (err) {
        console.log(err);
        this.$buefy.toast.open({
          message: "Có lỗi xảy ra!",
          type: "is-danger",
        });
      }
    },

    //
  },
};
</script>