<template>
  <div>
    <section>
      <div class="buttons">
        <b-button type="is-info" icon-left="file-document" @click="createDocs"
          >Thêm mới</b-button
        >
        <b-button type="is-info" icon-left="animation-outline"
          >Chia sẻ</b-button
        >
      </div>
    </section>
    <div>
      <b-tabs>
        <b-tab-item label="Tạo tài liệu">
          <section>
            <b-field
              v-if="!isCheck"
              label="Tên văn bản"
              custom-class="is-medium"
            >
              <b-input
                v-model="document.title"
                type="text"
                placeholder="Tên văn bản"
              ></b-input>
            </b-field>
            <b-field label="Tài liệu" custom-class="is-medium">
              <!-- <client-only> -->
              <div id="pdfDom" class="content" ref="content">
                <vue-editor v-model="document.content"></vue-editor>
              </div>
              <!-- </client-only> -->
            </b-field>

            <b-field
              v-if="isCheck"
              label="Tài liệu sau chỉnh sửa"
              custom-class="is-medium"
            >
              <!-- <client-only> -->
              <div class="content">
                <vue-editor v-model="content"></vue-editor>
              </div>

              <!-- </client-only> -->
            </b-field>

            <b-field>
              <div class="buttons">
                <b-button type="is-info" @click="updateDoc"
                  >Sửa văn bản</b-button
                >
                <b-button type="is-success" @click="checkDoc"
                  >Kiểm tra văn bản</b-button
                >
                <b-button type="is-danger" @click="deleteDoc"
                  >Xóa văn bản</b-button
                >
                <b-button
                  type="is-danger"
                  @click="getPdf(document.title, document.content)"
                  >Xuất ra PDF</b-button
                >
              </div>
            </b-field>
          </section>
        </b-tab-item>
      </b-tabs>
    </div>
    <b-notification ref="element" :closable="false">
      <b-loading
        :is-full-page="isFullPage"
        v-model="isLoading"
        :can-cancel="true"
      ></b-loading>
    </b-notification>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  layout: "default",
  name: "docs-id",
  data() {
    return {
      user: null,
      isLoading: false,
      isFullPage: true,
      isCheck: false,
      content: "",
      document: {
        title: "",
        content: "",
      },
      error: "",
      id_doc: {},
    };
  },
  async created() {
    this.user = this.$auth.$storage.getUniversal("user");
    this.id_doc = this.$route.params.id;

    const id = {
      id: this.id_doc,
    };
    const { isSuccess } = await this.getDocsById(id);
    if (isSuccess) {
      this.document = Object.assign({}, this.doc);
    }
  },
  computed: {
    ...mapState("docs", [
      "doc",
      "dataDeleteDoc",
      "dataUpdateDoc",
      "dataCorrect",
    ]),
  },
  methods: {
    ...mapActions("docs", [
      "getDocsById",
      "deleteDoc",
      "updateDocument",
      "checkCorrectDoc",
    ]),

    async updateDoc() {
      if (this.isCheck === true) {
        this.document.content = this.content;
      }
      const { isSuccess } = await this.updateDocument(this.document);
      if (isSuccess) {
        this.error = "Cập nhật thành công";
        this.$buefy.dialog.alert({
          title: "Thông báo",
          message: this.error,
          type: "is-info",
          ariaModal: true,
        });
      } else {
        this.error = "Cập nhật chưa thành công";
        this.$buefy.dialog.alert({
          title: "Lỗi",
          message: this.error,
          type: "is-danger",
          ariaRole: "alertdialog",
          ariaModal: true,
        });
      }

      this.isCheck = false;
    },
    async deleteDoc() {
      this.document.is_deleted = 1;
      const { isSuccess } = await this.updateDocument(this.document);
      if (isSuccess) {
        setTimeout(() => {
          this.$router.push("/listdocs");
        }, 300);
      } else {
        this.error = "Xóa chưa thành công";
        this.$buefy.dialog.alert({
          title: "Lỗi",
          message: this.error,
          type: "is-danger",
          ariaRole: "alertdialog",
          ariaModal: true,
        });
      }
    },

    async checkDoc() {
      const loadingComponent = this.$buefy.loading.open({
        container: this.isFullPage ? null : this.$refs.element.$el,
      });
      setTimeout(() => loadingComponent.close(), 4 * 1000);
      const dataRq = {
        content: this.document.content,
      };
      console.log(this.document.content);
      const { isSuccess } = await this.checkCorrectDoc(dataRq);
      if (isSuccess) {
        this.isCheck = true;
        this.content = this.dataCorrect.content;
      }
    },
    open() {
      const loadingComponent = this.$buefy.loading.open({
        container: this.isFullPage ? null : this.$refs.element.$el,
      });
      setTimeout(() => loadingComponent.close(), 1 * 1000);
    },
  },
};
</script>

<style scoped>
.content {
  background-color: azure;
}
</style>