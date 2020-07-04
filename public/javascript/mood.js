const moodbtns = document.querySelectorAll('.Button');

// colors orange #F6914F
// colors blue #93A3ED
// colors purple #b8b8f4
// colors see green #64BCDE
// colors yellow #F9CA79
// colors pink #F9CCE4
colors = {
  love: '#F9CCE4',
  lonely: '#b8b8f4',
  sad: '#F6914F',
  happy: '#F9CA79',
  anxious: '#64BCDE',
  relaxed: '#93A3ED',
};
let currMood = 'anxious';
const handleMoodClick = (e) => {
  const lableTarget = e.target.getAttribute('for');
  console.log(lableTarget);
  currMood = document.querySelector(`#${lableTarget}`).value;
  console.log(currMood);
  document.querySelector(`.face`).src = `images/faces/${currMood}.png`;
  document.querySelector('.smile-area').style.backgroundColor =
    colors[currMood];
};

moodbtns.forEach((btn) => btn.addEventListener('click', handleMoodClick));
