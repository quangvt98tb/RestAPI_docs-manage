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
          readonly
        ></b-input>
      </b-field>

      <b-field label="Thể loại" custom-class="is-medium" v-if="!isSelect">
        <b-input v-model="category_doc" type="text" readonly></b-input>
      </b-field>

      <b-field label="Văn bản" custom-class="is-medium" readonly>
        <div class="content">
          <vue-editor
            v-model="text"
            :editorToolbar="customToolbar"
          ></vue-editor>
        </div>
      </b-field>

      <b-field>
        <div class="buttons">
          <b-button type="is-info">Xuất ra PDF</b-button>
        </div>
      </b-field>

      <b-field label="Bình luận" custom-class="is-medium">
        <div class="card">
          <div class="card-content">
            <!-- <div class="subtitle"></div> -->
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
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
var _ = require("lodash");
import axios from "axios";

export default {
  layout: "default",
  name: "docs-share-read-id",
  data() {
    return {
      user: null,
      email: null,
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
        id_user: null,
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
    ...mapState("comment", ["list_comment"]),
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
    ...mapActions("comment", ["listComment"]),
    // create -doc
    createDocs() {
      setTimeout(() => {
        this.$router.push("/docs/create-doc");
      }, 500);
    },
    // tesst

    // share - doc

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