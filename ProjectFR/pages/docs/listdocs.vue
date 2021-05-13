<template>
  <div>
    <section>
      <div class="buttons">
        <b-button type="is-info" icon-left="file-document" @click="createDocs"
          >Thêm mới</b-button
        >
        <!-- <b-button type="is-info" icon-left="animation-outline"
          >Chia sẻ</b-button
        > -->
      </div>
    </section>
    <section>
      <b-tabs>
        <b-tab-item label="Tài liệu của bạn">
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
            @click="updateDoc"
          >
          </b-table>
        </b-tab-item>
        <b-tab-item label="Tài liệu chia sẻ (chỉ đọc)">
          <DocsTable
            :data="listDocsRead"
            :columns="columns"
            :selected="selectedRead"
            @pick="readDoc"
          />
        </b-tab-item>
        <b-tab-item label="Tài liệu chia sẻ (chỉnh sửa)">
          <DocsTable
            :data="listDocsFix"
            :columns="columns"
            :selected="selectedFix"
            @pick="fixDoc"
          />
        </b-tab-item>
      </b-tabs>
      <!-- <b-notification :closable="false">
        <b-loading
          :is-full-page="isFullPage"
          v-model="isLoading"
          :can-cancel="true"
        >
          <b-icon
            pack="fas"
            icon="sync-alt"
            size="is-large"
            custom-class="fa-spin"
          >
          </b-icon>
        </b-loading>
      </b-notification> -->
    </section>
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
      user: null,
      data: [],
      isLoading: false,
      isFullPage: true,
      selected: null,
      isPaginated: true,
      currentPage: 1,
      perPage: 7,
      defaultSortDirection: "asc",
      isPaginationSimple: false,
      isPaginationRounded: true,
      paginationPosition: "bottom",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",

      listDocsFix: [],
      selectedFix: {},
      listDocsRead: [],
      selectedRead: {},

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
          field: "user_update_last",
          label: "Người chỉnh cuối",
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
    const { isSuccess } = await this.getListDocsById(inp);
    if (isSuccess) {
      this.data = this.dataDocs;
      this.selected = this.data[0];
    } else {
      this.data = [];
    }

    const res1 = await this.getListDocsShareFix(inp);
    if (res1.isSuccess) {
      this.listDocsFix = this.listShareFix;
      console.log(this.listDocsFix);
      this.selectedFix = this.listDocsFix[0];
    } else {
      this.listDocsFix = [];
    }

    const res2 = await this.getListDocsShareRead(inp);
    console.log(this.listShareRead);
    if (res2.isSuccess) {
      this.listDocsRead = this.listShareRead;
      this.selectedRead = this.listDocsRead[0];
    } else {
      this.listDocsRead = [];
    }
  },
  computed: {
    ...mapState("docs", ["dataDocs", "listShareFix", "listShareRead"]),
  },
  methods: {
    ...mapActions("docs", [
      "getListDocsById",
      "getListDocsShareFix",
      "getListDocsShareRead",
    ]),
    createDocs() {
      setTimeout(() => {
        this.$router.push("/docs/create-doc");
      }, 500);
    },

    updateDoc() {
      this.isLoading = true;
      setTimeout(() => {
        this.isLoading = false;
      }, 1000);

      setTimeout(() => {
        this.$router.push({
          name: "docs-id",
          params: {
            id: this.selected.id,
          },
        });
      }, 100);
    },

    readDoc() {
      this.isLoading = true;
      setTimeout(() => {
        this.isLoading = false;
      }, 1000);

      setTimeout(() => {
        this.$router.push({
          name: "docs-share-read-id",
          params: {
            id: this.selectedRead.id,
          },
        });
      }, 100);
    },

    fixDoc() {
      this.isLoading = true;
      setTimeout(() => {
        this.isLoading = false;
      }, 1000);

      setTimeout(() => {
        this.$router.push({
          name: "docs-share-fix-id",
          params: {
            id: this.selectedFix.id,
          },
        });
      }, 100);
    },
  },
};
</script>