<template>
  <div class="columns is-mobile">
    <div class="column is-three-quarters">
      <b-field label="Tên văn bản" custom-class="is-medium">
        <b-input
          v-model="title"
          type="text"
          placeholder="Tên văn bản"
        ></b-input>
      </b-field>

      <b-field label="Thể loại" custom-class="is-medium">
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
        ></b-input>
      </b-field>

      <b-field>
        <b-button type="is-success" @click="createDocument()">
          Lưu văn bản
        </b-button>
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
  data() {
    return {
      user: null,
      category: [],
      dataReq: {
        title: "",
        content: "",
        category_id: null,
        is_deleted: 0,
        id_author: null,
        update_last_by: null,
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
      categoryId: [],
      list: ["1", "2"],
    };
  },
  watch: {
    text: function () {
      if (this.isCheck) {
        this.list = [];
        this.getSuggest();
      }
    },
  },

  async created() {
    // get id user
    this.user = this.$auth.$storage.getUniversal("user");
    this.dataReq.id_author = this.user.id;
    // get list category
    const { isSuccess } = await this.listCategory();
    if (isSuccess) {
      this.category = this.list_category;
    } else {
      this.category = [];
    }
  },
  computed: {
    ...mapState("category", ["list_category"]),
    ...mapState("docs", ["dataCreateDoc", "dataCorrect"]),
  },
  methods: {
    ...mapActions("category", ["listCategory"]),
    ...mapActions("docs", ["createDocument", "checkCorrectDoc"]),

    async createDocument() {
      this.dataReq.title = this.title;
      this.dataReq.content = this.text;
      this.dataReq.category_id = this.categoryId;
      this.dataReq.is_deleted = 0;
      this.dataReq.update_last_by = this.dataReq.id_author;
      console.log(this.dataReq);

      const { isSuccess } = await this.createDocument(this.dataReq);
      if (isSuccess) {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Tạo thành công!",
            type: "is-success",
          });
        }, 500);
      } else {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Tạo không thành công!",
            type: "is-danger",
          });
        }, 1000);
      }
    },

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
  mounted() {
    this.isMounted = true;
  },
};
</script>

<style scoped>
</style>