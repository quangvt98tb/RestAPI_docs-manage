<template>
  <div class="columns is-mobile">
    <div class="column is-three-quarters">
      <b-field>
        <section>
          <div class="buttons">
            <b-button
              type="is-info"
              icon-left="file-document"
              style="float: right"
              @click="createDocs"
              >Thêm mới</b-button
            >
          </div>
        </section>
      </b-field>

      <br />
      <b-field label="Tên văn bản" custom-class="is-medium">
        <b-input
          v-model="title"
          type="text"
          placeholder="Tên văn bản"
        ></b-input>
      </b-field>

      <b-field label="Thể loại" custom-class="is-medium" v-if="!isSelect">
        <b-input v-model="category_doc" type="text" disabled></b-input>
      </b-field>

      <b-field label="Thể loại" custom-class="is-medium" v-if="isSelect">
        <b-select
          placeholder="Chọn thể loại"
          v-model="categoryId"
          rounded
          expanded
          required
        >
          <option
            v-for="(item, index) in category"
            :key="index"
            :value="item.id"
          >
            {{ item.name_category }}
          </option>
        </b-select>
      </b-field>

      <b-field custom-class="is-medium">
        <b-checkbox v-model="isSelect">Chỉnh sửa thể loại</b-checkbox>
      </b-field>

      <b-field custom-class="is-medium">
        <b-checkbox v-model="isCheck"> Kiểm tra chính tả </b-checkbox>
      </b-field>

      <b-field label="Văn bản" custom-class="is-medium">
        <div class="content">
          <vue-editor
            v-model="text"
            :editorToolbar="customToolbar"
          ></vue-editor>
        </div>
      </b-field>

      <b-field label="Văn bản raw" custom-class="is-medium">
        <b-input
          type="textarea"
          v-model="text"
          placeholder="Viết gì đó..."
          readonly
        ></b-input>
      </b-field>

      <b-field>
        <div class="buttons">
          <b-button type="is-success" @click="updateDoc">
            Lưu văn bản
          </b-button>

          <b-button type="is-info">Xuất ra PDF</b-button>
        </div>
      </b-field>

      <b-field label="Đánh giá - Bình luận" custom-class="is-medium">
        <b-input
          type="textarea"
          v-model="cmt"
          placeholder="Viết gì đó..."
        ></b-input>
      </b-field>
      <b-field>
        <b-button type="is-info" @click="commnet">Bình luận</b-button>
      </b-field>

      <b-field label="Các bình luận" custom-class="is-medium">
        <div class="card">
          <div class="card-content">
            <div class="content">
              <section>
                <b-message
                  type="is-info"
                  size="is-small"
                  v-for="(item, index) in comments"
                  :key="index"
                >
                  {{ item.comment }}
                  <p>
                    Bởi <i>{{ item.user_email }}</i>
                  </p>
                </b-message>
              </section>
            </div>
          </div>
        </div>
      </b-field>
    </div>

    <div v-if="isCheck" class="column check">
      <div class="card">
        <div class="card-content">
          <div class="subtitle">Kiểm tra chính tả</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
var _ = require("lodash");
import axios from "axios";

export default {
  layout: "default",
  name: "docs-share-fix-id",
  data() {
    return {
      user: null,
      email: null,
      cmt: null,
      role: 0,
      isSelect: false,
      isShare: false,
      category_doc: null,
      category: [],
      comments: [],
      dataReq: {
        title: "",
        content: "",
        category_id: null,
        is_deleted: 0,
      },
      isMounted: false,
      isCheck: false,
      messages: [],
      customToolbar: [
        ["bold", "italic"],
        [
          { align: "" },
          { align: "center" },
          { align: "right" },
          { align: "justify" },
        ],
        [{ list: "ordered" }, { list: "bullet" }],
        ["clean"], // remove formatting button
      ],
      text: "",
      title: "",
      document: {},
      categoryId: null,
      list: ["1", "2"],
    };
  },
  // watch
  watch: {
    text: function () {
      if (this.isCheck) {
        this.list = [];
        this.getSuggest();
      }
    },
  },

  //create
  async created() {
    this.user = this.$auth.$storage.getUniversal("user");
    this.id_doc = this.$route.params.id;

    await this.listCategory();

    this.category = this.list_category;

    const id = {
      id: this.id_doc,
    };
    await this.listComment(id);

    this.comments = this.list_comment;

    const { isSuccess } = await this.getDocsById(id);
    if (isSuccess) {
      this.document = Object.assign({}, this.doc);
      this.title = this.document.title;
      this.text = this.document.content;
      this.category_doc = this.document.category_name;
    }
  },

  //
  computed: {
    ...mapState("docs", [
      "doc",
      "dataDeleteDoc",
      "dataUpdateDoc",
      "dataCorrect",
      "dataShare",
    ]),
    ...mapState("category", ["list_category"]),
    ...mapState("comment", ["list_comment", "dataCreateComment"]),
  },
  methods: {
    ...mapActions("docs", [
      "getDocsById",
      "deleteDoc",
      "updateDocument",
      "checkCorrectDoc",
      "shareDoc",
    ]),
    ...mapActions("category", ["listCategory"]),
    ...mapActions("comment", ["listComment", "createComment"]),
    // create -doc
    createDocs() {
      setTimeout(() => {
        this.$router.push("/docs/create-doc");
      }, 500);
    },
    // create - comment
    async commnet() {
      let data = {
        id_user: this.user.id,
        id_doc: this.id_doc,
        comment: this.cmt,
      };
      const { isSuccess } = await this.createComment(data);
      if (isSuccess) {
        const id = {
          id: this.id_doc,
        };
        await this.listComment(id);

        this.comments = this.list_comment;
        this.$buefy.toast.open({
          message: "thành công!",
          type: "is-success",
        });
      } else {
        this.$buefy.toast.open({
          message: "không thành công!",
          type: "is-danger",
        });
      }
    },
    // update doc
    async updateDoc() {
      this.dataReq.id = this.document.id;
      this.dataReq.title = this.title;
      this.dataReq.content = this.text;
      this.dataReq.is_deleted = 0;
      this.dataReq.id_author = this.document.id_author;
      this.dataReq.update_last_by = this.user.id;
      this.dataReq.created = this.document.created;
      this.dataReq.updated = this.document.updated;
      this.dataReq.category_id = this.document.category_id;

      if (this.isSelect) {
        this.dataReq.category_id = this.categoryId;
        for (let index = 0; index < this.category.length; index++) {
          if (this.dataReq.category_id === this.category[index].id) {
            this.document.category_id = this.category[index].id;
            this.category_doc = this.category[index].name_category;
            this.document.category_name = this.category_doc;
          }
        }
      } else {
        this.dataReq.category_id = this.document.category_id;
      }
      console.log(this.dataReq);
      const { isSuccess } = await this.updateDocument(this.dataReq);
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
    },

    // spelling
    getSuggest: _.debounce(
      async function () {
        if (this.text == "") {
          this.list = [];
          return;
        }
      },
      // Đây là thời gian (đơn vị mili giây) đợi người dùng dừng gõ.
      2500
    ),
  },
};
</script>

<style scoped>
/* .content {
  background-color: azure;
} */
</style>