<template>
  <div class="navi">
    <b-navbar>
      <template #brand>
        <b-navbar-item>
          <img
            src="/logoBIT.png"
            alt="logo team BIT"
            style="padding-left: 60px"
          />
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-field>
          <div style="padding-left: 300px">
            <b-autocomplete
              type="is-info"
              placeholder="Search..."
              clearable
              icon="magnify"
              expanded
            >
            </b-autocomplete>
          </div>
        </b-field>
      </template>

      <template slot="end">
        <b-navbar-item>
          <b-field><b-icon icon="lightbulb"></b-icon></b-field>
        </b-navbar-item>
      </template>
    </b-navbar>
  </div>
</template>
<style scoped>
.navi {
  background-color: rgba(var(--b3f, 240, 255, 255), 1);
  border-bottom: 2px solid rgba(var(--b3f, 217, 217, 217), 1);
}
</style>