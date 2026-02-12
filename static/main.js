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

  // ✅ 你要“根据客户实际输入动态显示”的地方：改这里即可
  function makeBasicResult(input){
    const v = (input || "").trim();
    const hasNumber = /\d/.test(v);

    // 这里先做演示规则：你未来换成 fetch 后端也就在这里换
    return {
      type: hasNumber ? `コード入力：${v}` : `名称入力：${v}`,
      risk: hasNumber ? "中（参考）" : "低〜中（参考）",
      note: "公開情報を元にした要約表示です。詳細はLINEで確認できます。"
    };
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

    if (!form || !q) return; // 非首页不跑

    // ✅ 提交：显示基础结果（先给用户看到）
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const v = (q.value || "").trim();
      if(!v){
        alert("キーワードを入力してください。");
        return;
      }

      const r = makeBasicResult(v);

      resultQuery.textContent = `入力：${v}`;
      rType.textContent = r.type;
      rRisk.textContent = r.risk;
      rNote.textContent = r.note;

      resultWrap.style.display = "block";
      resultWrap.scrollIntoView({behavior:"smooth", block:"start"});
    });

    // ✅ 你之前按钮没反应：就靠这段绑定
    if (openLineModalBtn) {
      openLineModalBtn.addEventListener('click', function (e) {
        e.preventDefault();
        openModal(modal);
      });
    }

    // ✅ 关闭弹窗：遮罩 / X / ESC
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

    // ✅ 重新输入
    if (resetBtn) {
      resetBtn.addEventListener('click', function(){
        q.value = "";
        q.focus();
        resultWrap.style.display = "none";
      });
    }

    // ✅ mini 搜索框：把 q2 填回 q 并触发主表单
    if (miniForm && q2) {
      miniForm.addEventListener('submit', function(e){
        e.preventDefault();
        const v = (q2.value || "").trim();
        if(!v) return;

        q.value = v;
        form.requestSubmit(); // 触发主表单提交
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
    document.body.style.overflow = "hidden"; // prevent background scroll
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

  // close after clicking any link
  drawer.querySelectorAll("a").forEach(a => a.addEventListener("click", close));
})();