const siteHeader = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-button');
const navActions = document.querySelector('.nav-actions');
const navLinks = document.querySelectorAll('.nav-links a, .hero-actions a, .brand');
const themeButton = document.querySelector('.theme-button');
const scrollTopButton = document.querySelector('#scroll-top');
const projectStatus = document.querySelector('#project-status');
const projectsList = document.querySelector('#projects-list');
const retryButton = document.querySelector('#retry-button');
const contactForm = document.querySelector('#contact-form');
const formSuccess = document.querySelector('#form-success');
const formFields = document.querySelectorAll('#name, #email, #message');

const setTheme = (theme) => {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  themeButton.textContent = theme === 'dark' ? 'Light' : 'Dark';
};

const savedTheme = localStorage.getItem('theme');
setTheme(savedTheme === 'dark' ? 'dark' : 'light');

themeButton.addEventListener('click', () => {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});

menuButton.addEventListener('click', () => {
  const isOpen = navActions.classList.toggle('active');
  menuButton.setAttribute('aria-expanded', isOpen);
  menuButton.setAttribute('aria-label', isOpen ? '메뉴 닫기' : '메뉴 열기');
});

navLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    const targetId = link.getAttribute('href');
    const target = document.querySelector(targetId);
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: 'smooth' });
    navActions.classList.remove('active');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', '메뉴 열기');
  });
});

const updateScrollUi = () => {
  const currentScroll = window.scrollY;
  if (currentScroll >= 60) siteHeader.classList.add('scrolled');
  else siteHeader.classList.remove('scrolled');

  if (currentScroll >= 300) scrollTopButton.classList.add('visible');
  else scrollTopButton.classList.remove('visible');
};

window.addEventListener('scroll', updateScrollUi);
updateScrollUi();
scrollTopButton.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

const loadProjects = async () => {
  projectStatus.textContent = '프로젝트를 불러오는 중...';
  projectsList.innerHTML = '';
  retryButton.hidden = true;

  try {
    const response = await fetch('https://api.github.com/users/hay-dev2024/repos');
    if (!response.ok) throw new Error('GitHub API request failed');
    const repositories = await response.json();

    if (repositories.length === 0) {
      projectStatus.textContent = '표시할 프로젝트가 없습니다.';
      return;
    }

    projectsList.innerHTML = repositories.map(({ name, description, language, stargazers_count, html_url }) => `
      <article class="project-card">
        <h3>${name}</h3>
        <p>${description || '저장소 설명이 없습니다.'}</p>
        <p class="project-meta">언어: ${language || '정보 없음'} · Stars: ${stargazers_count}</p>
        <a class="project-link" href="${html_url}" target="_blank" rel="noopener noreferrer">GitHub에서 보기</a>
      </article>
    `).join('');
    projectStatus.textContent = `${repositories.length}개의 프로젝트를 표시합니다.`;
  } catch (error) {
    projectStatus.textContent = '프로젝트를 불러올 수 없습니다.';
    retryButton.hidden = false;
  }
};

retryButton.addEventListener('click', loadProjects);
loadProjects();

const validateField = (field) => {
  const errorElement = document.querySelector(`#${field.id}-error`);
  const value = field.value.trim();
  let errorMessage = '';

  if (!value) errorMessage = '필수 입력 항목입니다.';
  else if (field.id === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) errorMessage = '올바른 이메일 형식을 입력해 주세요.';

  errorElement.textContent = errorMessage;
  field.classList.toggle('input-error', Boolean(errorMessage));
  return !errorMessage;
};

formFields.forEach((field) => {
  field.addEventListener('input', () => {
    validateField(field);
    formSuccess.textContent = '';
  });
});

contactForm.addEventListener('submit', (event) => {
  event.preventDefault();
  let isValid = true;
  formFields.forEach((field) => {
    if (!validateField(field)) isValid = false;
  });

  if (isValid) {
    formSuccess.textContent = '메시지가 정상적으로 확인되었습니다.';
    contactForm.reset();
  }
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.2 });

document.querySelectorAll('.reveal').forEach((section) => observer.observe(section));
