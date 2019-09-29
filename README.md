## 1Sasha1MarkdownNoBBCode
Sublime Text 3 Plugin to inline convert markdown to BBCode

## Usage

Ctrl+Shift+P → 1Sasha1MarkdownNoBBCode: Convert Markdown To BBCode → your markdown file will be convert to BBCode.


## Installation

### By Package Control

1. Download & Install `Sublime Text 3` (https://www.sublimetext.com/3)
1. Go to the menu `Tools -> Install Package Control`, then,
   wait few seconds until the `Package Control` installation finishes
1. Go to the menu `Preferences -> Package Control`
1. Type `Package Control Add Channel` on the opened quick panel and press <kbd>Enter</kbd>
1. Then, input the following address and press <kbd>Enter</kbd>
   ```
   https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
   ```
1. Now, go again to the menu `Preferences -> Package Control`
1. This time type `Package Control Install Package` on the opened quick panel and press <kbd>Enter</kbd>
1. Then, search for `MarkdownToBBCode` and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


## Example

### Markdown

	<http://anima-kommunizm.forum2x2.ru/t197-topic>

	__Сумрак, корабль _гудит_ на Стокгольм,
	как снова взыграла *Любовь*,
	~~что выгодно исстарь ему —
	настырную "шизу" забанить,
	не отягощать [зазря](http://facelessuser.github.io/FindCursor/usage/#settings) память,~~ —
	вовек обещала прильнув,__

	---

	~~Кот~~

	_теперь точно всё хорошо,
	романтикой веет с __Луной__,
	"[защитник людей](http://stackoverflow.com/questions/587345/python-regular-expression-matching-a-multiline-block-of-text)" Твой герой,
	гнев не получающий_

	**"Плохо,
	смрад *скунса* от каждого вздоха,
	слюна брызжет ядом питоху",
	чем пуще в Тебе зреешь [Бога](http://facelessuser.github.io/FindCursor/usage/#settings),**

	*тем паче снедаешь жестоко,
	за что ни [возьмёшься](http://facelessuser.github.io/FindCursor/usage/#settings) — не трогай,
	растерян, податься куда:
	для **Кирочки** плохо всегда.*

	![Святое место](http://i21.servimg.com/u/f21/17/58/26/07/yeiae10.jpg)

	> Раз *плюнуть* без угрызений в людей, ярлык понавешивал "ват", и даже никнейм — сплошной мат — **Тебя** ни на [грамм](http://facelessuser.github.io/FindCursor/usage/#settings) не смущает, под _палкой для селфи_ печали нет в __чистых озёрах очей__,

	> пока меж *маньяков*, _клещей_
	> в тюрьму я [Тобою](http://facelessuser.github.io/FindCursor/usage/#settings) засажен,
	> для общества **обеззаражен**, —
	> __дай пять__ хамам, вторящим

	За `чуждых стихов *копипаcту* одариваешь _комплиментом_, в глубоком почтении "гений", [постигнувший](http://facelessuser.github.io/FindCursor/usage/#settings) воздух упругим`,

	```
	**сравнив** со *спасательным кругом*,
	_слова_ в текст __связать не умея__,
	[неприкосновенна](http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm) "легенда" —
	моим строкам место — _анамнез_,
	```

	    **Самой** сочинённый *нелепым глаголом*,
	    в отсутствии [прочего](http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm) жажду который
	    из __уст сладких__ внемлить, прервётся как скоро
	    _молчание_ их стародавнее _гроул(м)ом_

		__Твои__ *парни* сзади смеялись, по почкам
		_вложиться готовые_ сиюминутно
		чуть двинулся б я в вожделении подспудном
		ниц жадно припасть к **беломраморным ножкам**,
		[по вене Любви целовать веко Божье](http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm)

	+ _по тегам_ *залайканное* [url=http://ru.stackoverflow.com/editing-help]Инстаграма[/url],
	+ где отретушированное программой, —
	+ отныне наигранные **чувства** __гложут__,

	- морозам на **акциях** __зоозащитных__
	- предпочтены [атараксия](http://facelessuser.github.io/FindCursor/usage/#settings) и опыт,
	- _умалчивать боли_ нормально, солидно,
	- достал я, *лгун мелкий*, мешаю комфорту,

	* покину, коль просишь, зальёт **крови** __плазма__
	* асфальт [новгородский](http://facelessuser.github.io/FindCursor/usage/#settings), — _раздалось_ "*ужасно*"...

	# Нет
	## Отстаньте от меня
	### Вас [это](http://facelessuser.github.io/FindCursor/usage/#settings) не касается
	#### Сто раз сказала

	1. При звуках сих **неразделённых**
	2. Крест [безаргументационно](http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm)
	3. Поставишь, __признав__ меня *гноем*,
	4. _Судила_ как за остальное.

### BBCode

	[url]http://anima-kommunizm.forum2x2.ru/t197-topic[/url]

	[b]Сумрак, корабль [i]гудит[/i] на Стокгольм,
	как снова взыграла [i]Любовь[/i],
	[s]что выгодно исстарь ему —
	настырную "шизу" забанить,
	не отягощать [url=http://facelessuser.github.io/FindCursor/usage/#settings]зазря[/url] память,[\s] —
	вовек обещала прильнув,[/b]

	[hr]

	[s]Кот[\s]

	[i]теперь точно всё хорошо,
	романтикой веет с [b]Луной[/b],
	"[url=http://stackoverflow.com/questions/587345/python-regular-expression-matching-a-multiline-block-of-text]защитник людей[/url]" Твой герой,
	гнев не получающий[/i]

	[b]"Плохо,
	смрад [i]скунса[/i] от каждого вздоха,
	слюна брызжет ядом питоху",
	чем пуще в Тебе зреешь [url=http://facelessuser.github.io/FindCursor/usage/#settings]Бога[/url],[/b]

	[i]тем паче снедаешь жестоко,
	за что ни [url=http://facelessuser.github.io/FindCursor/usage/#settings]возьмёшься[/url] — не трогай,
	растерян, податься куда:
	для [b]Кирочки[/b] плохо всегда.[/i]

	[img]http://i21.servimg.com/u/f21/17/58/26/07/yeiae10.jpg[/img]

	[quote]Раз [i]плюнуть[/i] без угрызений в людей, ярлык понавешивал "ват", и даже никнейм — сплошной мат — [b]Тебя[/b] ни на [url=http://facelessuser.github.io/FindCursor/usage/#settings]грамм[/url] не смущает, под [i]палкой для селфи[/i] печали нет в [b]чистых озёрах очей[/b],[/quote]

	[quote]пока меж [i]маньяков[/i], [i]клещей[/i]
	в тюрьму я [url=http://facelessuser.github.io/FindCursor/usage/#settings]Тобою[/url] засажен,
	для общества [b]обеззаражен[/b], —
	[b]дай пять[/b] хамам, вторящим[/quote]

	За [code]чуждых стихов [i]копипаcту[/i] одариваешь [i]комплиментом[/i], в глубоком почтении "гений", [url=http://facelessuser.github.io/FindCursor/usage/#settings]постигнувший[/url] воздух упругим[/code],

	[code]
	[b]сравнив[/b] со [i]спасательным кругом[/i],
	[i]слова[/i] в текст [b]связать не умея[/b],
	[url=http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm]неприкосновенна[/url] "легенда" —
	моим строкам место — [i]анамнез[/i],
	[/code]

	[code][b]Самой[/b] сочинённый [i]нелепым глаголом[/i],
	в отсутствии [url=http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm]прочего[/url] жажду который
	из [b]уст сладких[/b] внемлить, прервётся как скоро
	[i]молчание[/i] их стародавнее [i]гроул(м)ом[/i][/code]

	[code][b]Твои[/b] [i]парни[/i] сзади смеялись, по почкам
	[i]вложиться готовые[/i] сиюминутно
	чуть двинулся б я в вожделении подспудном
	ниц жадно припасть к [b]беломраморным ножкам[/b],
	[url=http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm]по вене Любви целовать веко Божье[/url][/code]

	[list]
	[*][i]по тегам[/i] [i]залайканное[/i] [url=http://ru.stackoverflow.com/editing-help]Инстаграма[/url],
	[*]где отретушированное программой, —
	[*]отныне наигранные [b]чувства[/b] [b]гложут[/b],
	[/list]

	[list]
	[*]морозам на [b]акциях[/b] [b]зоозащитных[/b]
	[*]предпочтены [url=http://facelessuser.github.io/FindCursor/usage/#settings]атараксия[/url] и опыт,
	[*][i]умалчивать боли[/i] нормально, солидно,
	[*]достал я, [i]лгун мелкий[/i], мешаю комфорту,
	[/list]

	[i] покину, коль просишь, зальёт [b]крови[/b] [b]плазма[/b]
	[/i] асфальт [url=http://facelessuser.github.io/FindCursor/usage/#settings]новгородский[/url], — [i]раздалось[/i] "[i]ужасно[/i]"...

	[h1]Нет[/h1]
	[h2]Отстаньте от меня[/h2]
	[h3]Вас [url=http://facelessuser.github.io/FindCursor/usage/#settings]это[/url] не касается[/h3]
	[h4]Сто раз сказала[/h4]

	[list=1]
	[*]При звуках сих [b]неразделённых[/b]
	[*]Крест [url=http://radikal.ru/lfp/s018.radikal.ru/i509/1511/4b/383a15bcc0a7.jpg/htm]безаргументационно[/url]
	[*]Поставишь, [b]признав[/b] меня [i]гноем[/i],
	[*][i]Судила[/i] как за остальное.
	[/list]



