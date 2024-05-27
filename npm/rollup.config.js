// rollup.config.js
import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import typescript from "@rollup/plugin-typescript";
import dts from "rollup-plugin-dts";
import terser from "@rollup/plugin-terser";
import peerDepsExternal from "rollup-plugin-peer-deps-external";

const packageJson = require("./package.json");

export default [
  {
    input: "index.ts",
    output: [
      {
        file: packageJson.main,
        format: "cjs",
        sourcemap: true,
      },
      {
        file: packageJson.module,
        format: "esm",
        sourcemap: true,
      },
    ],
    plugins: [
      peerDepsExternal(),
      resolve(),
      commonjs(),
      typescript({ tsconfig: "./tsconfig.json" }),
      terser(),
    ],
    external: ["react", "react-dom"],
  },
  {
    input: "index.ts",
    output: [{ file: "dist/types.d.ts", format: "es" }],
    plugins: [dts.default()],
  },
  {
    input: 'nametonode.ts',
    output: [{
      file: 'dist/nametonode/index.js',
      format: 'esm',
      sourcemap: true,
    }]
  },
  {
    input: 'nametonode.ts',
    output: [{
      file: 'dist/nametonode/index.d.ts',
      format: 'es'
    }],
    plugins: [dts.default()],
  }
];