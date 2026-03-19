(function () {
  function qs(id) { return document.getElementById(id); }

  function openModal(modal){
    if(!modal) return;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
  }
  function closeModal(modal){
    if(!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
  }

  document.addEventListener('DOMContentLoaded', function () {
    const form = qs('stockForm');
    const q = qs('q');

    const resultWrap = qs('resultWrap');
    const resultQuery = qs('resultQuery');
    const rType = qs('rType');
    const rRisk = qs('rRisk');
    const rNote = qs('rNote');

    const openLineModalBtn = qs('openLineModal');
    const resetBtn = qs('resetBtn');

    const modal = qs('lineModal');

    // mini search
    const miniForm = qs('miniSearch');
    const q2 = qs('q2');

    if (form && q) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();

        const v = (q.value || "").trim();
        if(!v){
          alert("キーワードを入力してください。");
          return;
        }

        const r = {
          type: /\d/.test(v) ? `コード入力：${v}` : `名称入力：${v}`,
          risk: /\d/.test(v) ? "中（参考）" : "低〜中（参考）",
          note: "公開情報を元にした要約表示です。詳細はLINEで確認できます。"
        };

        if (resultQuery) resultQuery.textContent = `入力：${v}`;
        if (rType) rType.textContent = r.type;
        if (rRisk) rRisk.textContent = r.risk;
        if (rNote) rNote.textContent = r.note;

        if (resultWrap) {
          resultWrap.style.display = "block";
          resultWrap.scrollIntoView({behavior:"smooth", block:"start"});
        }
      });
    }

    if (openLineModalBtn) {
      openLineModalBtn.addEventListener('click', function (e) {
        e.preventDefault();
        openModal(modal);
      });
    }

    if (modal) {
      modal.addEventListener('click', function (e) {
        if (e.target && e.target.dataset && e.target.dataset.close === "1") {
          closeModal(modal);
        }
      });
      document.addEventListener('keydown', function(e){
        if(e.key === "Escape") closeModal(modal);
      });
    }

    if (resetBtn) {
      resetBtn.addEventListener('click', function(){
        if (q) q.value = "";
        if (q) q.focus();
        if (resultWrap) resultWrap.style.display = "none";
      });
    }

    if (miniForm && q2) {
      miniForm.addEventListener('submit', function(e){
        e.preventDefault();
        const v = (q2.value || "").trim();
        if(!v) return;

        if (q) q.value = v;
        if (form) form.requestSubmit();
      });
    }
  });
})();

// ===== Mobile Drawer Menu =====
(function () {
  const btn = document.getElementById("hamburgerBtn");
  const drawer = document.getElementById("mobileMenu");
  const backdrop = document.getElementById("drawerBackdrop");
  const closeBtn = document.getElementById("drawerCloseBtn");

  if (!btn || !drawer || !backdrop || !closeBtn) return;

  const open = () => {
    drawer.classList.add("open");
    backdrop.hidden = false;
    drawer.setAttribute("aria-hidden", "false");
    btn.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  };

  const close = () => {
    drawer.classList.remove("open");
    backdrop.hidden = true;
    drawer.setAttribute("aria-hidden", "true");
    btn.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  };

  btn.addEventListener("click", () => {
    const isOpen = drawer.classList.contains("open");
    isOpen ? close() : open();
  });

  closeBtn.addEventListener("click", close);
  backdrop.addEventListener("click", close);

  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });

  drawer.querySelectorAll("a").forEach(a => a.addEventListener("click", close));
})();

// ===== Desktop Dropdown Menus (支持多个下拉菜单) =====
(function () {
  const dropdowns = document.querySelectorAll('.nav-dropdown');

  dropdowns.forEach((dropdown) => {
    const toggle = dropdown.querySelector('.nav-dropdown-toggle');
    const menu = dropdown.querySelector('.dropdown-menu');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      dropdown.classList.toggle('open');

      // 关闭其他下拉菜单
      dropdowns.forEach((other) => {
        if (other !== dropdown) {
          other.classList.remove('open');
        }
      });
    });

    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function () {
        dropdown.classList.remove('open');
      });
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-dropdown')) {
      dropdowns.forEach((dropdown) => {
        dropdown.classList.remove('open');
      });
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      dropdowns.forEach((dropdown) => {
        dropdown.classList.remove('open');
      });
    }
  });

  window.addEventListener('resize', function () {
    dropdowns.forEach((dropdown) => {
      dropdown.classList.remove('open');
    });
  });
})();