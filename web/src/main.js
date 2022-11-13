/*
 * @Author: GoldenLandForever 108108205+GoldenLandForever@users.noreply.github.com
 * @Date: 2022-11-06 19:58:33
 * @LastEditors: GoldenLandForever 108108205+GoldenLandForever@users.noreply.github.com
 * @LastEditTime: 2022-11-07 11:23:37
 * @FilePath: \web\src\main.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import "bootstrap/dist/css/bootstrap.css"   
createApp(App).use(store).use(router).mount('#app');
