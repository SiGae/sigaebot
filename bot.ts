import config from "./config";
import Telegraf from "telegraf";
import dday from "./dday";

const answer: Array<string> = ["ㅇㅇ", "ㄴㄴ"];

let scnt: number = 0;

const run = () => {
  const bot = new Telegraf(config.API_KEY);

  bot.start((ctx) => ctx.reply("켜짐"));
  bot.command("ping", (ctx) => ctx.reply("test"));
  bot.command("clear", (ctx) => {
    let msg: string = "지워욧!";
    for (let i: number = 0; i < 20; i += 1) msg += "\n";
    msg += "요기까지";
    ctx.reply(msg);
  });
  bot.command("pick", (ctx) => {
    const pickList: Array<string> =
      ctx.message?.text?.toString().search(",") != -1
        ? (ctx.message?.text?.toString() + "").split(",")
        : ctx.message?.text?.toString().split(" ");
    delete pickList[0];
    ctx.reply(pickList[Math.floor(Math.random() * pickList.length)].trim());
  });
  bot.command("dday", async (ctx) => {
    ctx.reply(await dday(ctx.message?.text?.toString() + ""));
  });

  bot.on("message", (ctx) => {
    console.log(ctx.message);
    if (ctx.message?.text?.toString().search("마법의 소라고동") === 0) {
      ctx.reply(answer[Math.floor(Math.random() * 2)]);
    }

    if (
      ctx.message?.text?.toString() === "자야지" &&
      ctx.message.chat.id === 222521602
    )
      ctx.reply((scnt += 1).toString(), {
        reply_to_message_id: ctx.message.message_id,
      });
    const splitMsg: Array<string> = (ctx.message?.text?.toString() + "").split(
      " "
    );
    if (splitMsg[splitMsg.length - 1] === "확률은?")
      ctx.reply(Math.floor(Math.random() * 100).toString() + "퍼센트", {
        reply_to_message_id: ctx.message?.message_id,
      });
  });

  bot.launch();
};

run();
