<template>
  <div class="transition" :class="{animtrans: isActive}"></div>
  <div v-if="isShow" class="content">
    <h1>GPT신문에 오신 것을 환영합니다.</h1>
    <p>*GPT ai를 활용하여, 가독성 및 정확도가 떨어집니다.</p>
    <button @click="toggleClass" class="cta">신문 읽기</button>
  </div>
  <div v-if="!isShow" class="main">
    <h2 class="summary">{{ summary }}</h2>
    <div ref="wordCloud" class="wordcloud"></div>
    <div class="word-section">
      <h3>Positive Words</h3>
      <div ref="positiveWords" class="words-list"></div>
    </div>
    <div class="word-section">
      <h3>Negative Words</h3>
      <div ref="negativeWords" class="words-list"></div>
    </div>
  </div>
</template>

<script>
// Import local file
import wordData from "@/assets/response_1729483734840.json"; 
import cloud from "d3-cloud";
import * as d3 from "d3";

export default {
  name: "HelloWorld",
  data() {
    return {
      words: [], // Words for the word cloud
      summary: "", // Summary text from JSON
      positiveWords: [], // Positive words
      negativeWords: [], // Negative words
      isActive: false,
      isShow: true,
    };
  },
  mounted() {
     // Load data when component is mounted
  },
  methods: {
    fetchWordData() {
      const { wordcount, summary, positives, negatives } = wordData; // Extract data
      this.summary = summary; // Set summary text

      // Filter words between 5 and 40
      this.words = Object.keys(wordcount)
        .filter(word => wordcount[word] >= 5 && wordcount[word] <= 40 && word.length > 1)
        .map(word => {
          return {
            text: word,
            size: wordcount[word] * 2, // Set size from wordcount
          };
        });

      // Set positive and negative words
      this.positiveWords = positives || [];
      this.negativeWords = negatives || [];

      // Create the word cloud
      this.drawWordCloud();
      this.displayWords(); // Display positive and negative words
    },
    toggleClass() {
      if (this.isActive == true) return;
      this.isActive = true;
      setTimeout(() => {
        this.isShow = false;
        setTimeout(() => {
          this.fetchWordData();
        }, 1);
      }, 2000);
    },
    drawWordCloud() {
      const width = 500;
      const height = 500;

      const layout = cloud()
        .size([width, height])
        .words(this.words) // Use fetched words for word cloud
        .padding(5)
        .rotate(() => ~~(Math.random() * 2) * 90)
        .font("Impact")
        .fontSize(d => d.size) // Set size of each word
        .on("end", this.draw);

      layout.start();
    },
    draw(words) {
      const color = d3.scaleOrdinal(d3.schemeCategory10);

      d3.select(this.$refs.wordCloud)
        .append("svg")
        .attr("width", 500)
        .attr("height", 500)
        .append("g")
        .attr("transform", "translate(250,250)")  // Center alignment
        .selectAll("text")
        .data(words)
        .enter()
        .append("text")
        .style("font-size", d => `${d.size}px`)
        .style("fill", (d, i) => color(i))
        .style("cursor", "pointer")
        .attr("text-anchor", "middle")
        .attr("transform", d => `translate(${[d.x, d.y]})rotate(${d.rotate})`)
        .text(d => d.text)
        .on("click", (event, d) => {
          alert(`You clicked on: ${d.text}`);
        })
        .on("mouseover", function () {
          d3.select(this)
            .transition()
            .duration(200)
            .style("font-size", d => `${d.size * 1.1}px`);  // Slightly increase size
        })
        .on("mouseout", function () {
          d3.select(this)
            .transition()
            .duration(200)
            .style("font-size", d => `${d.size}px`);
        });
    },
    displayWords() {
      // Display positive words
      d3.select(this.$refs.positiveWords)
        .selectAll("div")
        .data(this.positiveWords)
        .enter()
        .append("div")
        .text(d => d)
        .style("color", "green"); // You can style it as needed

      // Display negative words
      d3.select(this.$refs.negativeWords)
        .selectAll("div")
        .data(this.negativeWords)
        .enter()
        .append("div")
        .text(d => d)
        .style("color", "red"); // You can style it as needed
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
.main {
  margin: 0 200px;
}
.wordcloud {
  width: 500px;
  height: 500px;
  margin: 0 auto;
}
.summary {
  text-align: center;
  font-size: 24px; /* Adjust font size for the summary */
}
.word-section {
  margin-top: 20px;
  text-align: center;
}
.words-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px; /* Adjust spacing between words */
}
.transition {
  position:absolute;
  height:100%;
  width:8%;
  background:#d6d6d6;
  transform: skewX(-5deg) translateX(-50px);
  transition:2s all ease-in-out;
  -webkit-transition:2s all ease-in-out;
}
.content {
  top: 30vh;
  position:relative;
  color:#000;
  z-index:10;
  height:300px;
}
.cta {
  outline:none;
  border:none;
  text-decoration:none;
  text-transform:uppercase;
  background:#202020;
  color:#eaeaea;
  box-sizing:border-box;
  margin-top:20px;
  padding:10px 40px;
}
.animtrans {
  animation: anim 4s ease-in-out;
}
@keyframes anim{
     0% { }
     20%  { z-index:11;\transform: skewX(5deg) translateX(-100%); }
     40%   { transform: skewX(0deg) translateX(0);
 width:100%; z-index:11; box-shadow: 10px 10px 5px #eaeaea;}
     60%   { transform: skewX(3deg) translateX(0);
 width:100%;z-index:11; box-shadow: 10px 10px 5px #eaeaea;}
     80%   { transform: skewX(1deg) translateX(-100%);
 width:50%;z-index:11; box-shadow: 10px 10px 5px #eaeaea;}
     100%   { transform: skewX(-5deg) translateX(-50px);
 width:8%;z-index:1; box-shadow: none;}
}
</style>
