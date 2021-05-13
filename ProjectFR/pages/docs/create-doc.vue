<template>
  <div class="columns is-mobile">
    <div class="column is-two-thirds">
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
        <b-checkbox v-model="isCheck">Kiểm tra chính tả </b-checkbox>
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
        <b-button type="is-success" @click="create()"> Lưu văn bản </b-button>
      </b-field>
    </div>

    <div v-if="isCheck" class="column check">
      <div class="card">
        <div class="card-content">
          <div class="subtitle">Kiểm tra chính tả tiếng việt</div>
          <div class="content">
            <b-button type="is-info" @click="checkDoc" expanded
              >Kiểm tra chính tả</b-button
            >
            <br />
            <div class="columns">
              <div class="column is-half">
                <b-field>
                  <b-tooltip label="Từ sau" position="is-bottom">
                    <b-button
                      icon-left="skip-previous"
                      @click="preword"
                    ></b-button>
                  </b-tooltip>
                  <b-tooltip label="Từ tiếp" position="is-bottom">
                    <b-button
                      icon-right="skip-next"
                      @click="nextword"
                    ></b-button>
                  </b-tooltip>
                </b-field>
                <b-field label="Thay thế:">
                  <b-input
                    v-model="word_fix.word"
                    type="text"
                    readonly
                  ></b-input>
                </b-field>
                <b-field label="Bởi:">
                  <b-input v-model="word_replace.word" type="text"></b-input>
                </b-field>
                <b-field label="Gợi ý">
                  <b-button type="is-success" @click="suggestWord" expanded>{{
                    word_suggest.word
                  }}</b-button>
                </b-field>
              </div>
              <div class="column is-half">
                <div class="buttons">
                  <b-button type="is-info" @click="fixSingle" expanded
                    >Sửa</b-button
                  >
                  <b-button type="is-info" @click="fixfull" expanded
                    >Sửa hết</b-button
                  >
                  <b-button type="is-danger" expanded>Bỏ qua</b-button>
                  <b-button type="is-danger" expanded>Bỏ qua hết</b-button>
                  <b-button type="is-success" expanded>Hoàn tất</b-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapState } from "vuex";
var _ = require("lodash");
import { joinSen } from "@/utils/joinsentence";
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
      isCheck: true,
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
      // correct
      list: [],
      fixfulltext: null,
      //
      listRaw: [],
      listCorrect: [],
      // list full
      list_raw: [],
      list_correct: [],
      //
      index_word: 0,
      word_fix: {
        index: 0,
        word: null,
        type: 0,
      },
      word_replace: { index: 0, word: null, type: 0 },
      word_suggest: {
        index: 0,
        word: null,
        type: 0,
      },
      list_t: [],
    };
  },
  watch: {
    // text: function () {
    //   if (this.isCheck) {
    //     this.list = [];
    //     this.getSuggest();
    //   }
    // },
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

    async create() {
      this.dataReq.title = this.title;
      this.dataReq.content = this.text;
      this.dataReq.category_id = this.categoryId;
      this.dataReq.is_deleted = 0;
      this.dataReq.update_last_by = this.dataReq.id_author;

      const { isSuccess } = await this.createDocument(this.dataReq);
      if (isSuccess) {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Tạo thành công!",
            type: "is-success",
          });
          this.$router.push("/docs/listdocs");
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
    // pick suggestWord
    suggestWord() {
      this.word_replace.word = this.word_suggest.word;
    },
    // check -spell
    async checkDoc() {
      this.isCheck = true;
      const dtr = {
        content: this.text,
      };
      const { isSuccess } = await this.checkCorrectDoc(dtr);
      if (isSuccess) {
        // this.text = this.dataCorrect.sentence_raw;
        this.fixfulltext = this.dataCorrect.sentence_all;
        this.list_raw = this.dataCorrect.list_raw;
        this.list_correct = this.dataCorrect.list_correct;
        this.listRaw = this.dataCorrect.listraw;
        this.listCorrect = this.dataCorrect.listcheck;

        // highlight text
        this.list_t = [];
        for (let ii = 0; ii < this.listRaw.length; ii++) {
          const el = Object.assign({}, this.listRaw[ii]);
          this.list_t.push(el);
        }
        if (this.list_raw.length > 0) {
          for (let j = 0; j < this.list_raw.length; j++) {
            const el_index = this.list_raw[j].index;

            this.list_t[el_index].word =
              `\<u\>` + this.list_t[el_index].word + `\<\/u\>`;
          }
        }

        let text_fix = joinSen(this.list_t);
        //
        this.text = text_fix;
        // this.text = this.dataCorrect.sentence_raw;
        this.fixfulltext = this.dataCorrect.sentence_all;
        this.list_raw = this.dataCorrect.list_raw;
        this.list_correct = this.dataCorrect.list_correct;
        this.listRaw = this.dataCorrect.listraw;
        this.listCorrect = this.dataCorrect.listcheck;

        if (this.list_raw.length > 0) {
          this.index_word = 0;
          this.word_fix = this.list_raw[0];
          this.word_suggest = this.list_correct[0];
          this.word_replace = Object.assign({}, this.word_fix);
        }
      } else {
        this.word_fix = {
          index: 0,
          word: null,
          type: 0,
        };
        this.word_replace = { index: 0, word: null, type: 0 };
        this.word_suggest = {
          index: 0,
          word: null,
          type: 0,
        };
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "Có lỗi xãy ra!",
            type: "is-danger",
          });
        }, 300);
      }
    },

    // next
    nextword() {
      const max_index = this.list_raw.length - 1;
      if (this.index_word < max_index) {
        this.index_word = this.index_word + 1;
        this.word_fix = this.list_raw[this.index_word];
        this.word_suggest = Object.assign(
          {},
          this.list_correct[this.index_word]
        );
        this.word_replace = Object.assign({}, this.word_fix);
      } else {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "!!!",
            type: "is-warning",
          });
        }, 300);
      }
    },
    // pre
    preword() {
      if (this.index_word > 0) {
        this.index_word = this.index_word - 1;
        this.word_fix = this.list_raw[this.index_word];
        this.word_suggest = Object.assign(
          {},
          this.list_correct[this.index_word]
        );
        this.word_replace = Object.assign({}, this.word_fix);
      } else {
        setTimeout(() => {
          this.$buefy.toast.open({
            message: "!!!",
            type: "is-warning",
          });
        }, 300);
      }
    },
    // fix single
    fixSingle() {
      //
      const index = this.word_fix.index;
      this.list_t[index] = this.word_replace;

      let text_fix = joinSen(this.list_t);

      this.text = text_fix;
    },
    // fix full
    fixfull() {
      this.text = this.fixfulltext;
    },
    // spelling
    getSuggest: _.debounce(
      async function () {
        if (this.text == "") {
          this.list = [];
          return;
        }
        if (_.endsWith(this.text, ".")) {
          this.list = [];
          return;
        }
        var endPosition = Number(this.text.lastIndexOf("."));
        if (endPosition === -1) {
          const textInput = this.text;
        } else {
          const textInput = this.text.slice(endPosition + 1);
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