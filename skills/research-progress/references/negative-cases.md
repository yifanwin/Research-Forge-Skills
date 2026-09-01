# Negative Cases（示意）

1. **直接解决**：深读最近工作发现问题、机制、评测均重合 → hard contradiction → 否决。
2. **资源未闭合**：价值成立但关键数据/接口拿不到 → repairable blocker → 卡住，不设计方法。
3. **机制被反驳**：隔离消融输给 baseline，完整系统却涨点 → 禁止外围续命；原 hypothesis 证伪，新机制须重立。
4. **范围爆炸**：benchmark、generator、value model、curriculum、adaptation 同时出现 → Minimal Claim Test 收敛一个 claim，其余暂存。

以上数字（如有）均为示意，不是实际实验结果。
