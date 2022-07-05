from manimlib import *
from os import system
from matplotlib.pyplot import title
import numpy as np


class Derivative(Scene):
    def construct(self):
        #视频标题部分

        introtext1 = Text(
        text="给初中生的导数介绍\n\n    二次函数篇",
        font="simsun",
        gradient=[BLUE, GREEN],
        t2w={"导数":BOLD},
        t2f={"导数":"msyh"}
        )
        introtext1.set_width(FRAME_WIDTH-2)
        self.play(Write(introtext1))
        self.wait(2)
        self.play(FadeOut(introtext1))

        #概念介绍部分
        title_intro = Title("介绍",color=BLACK,include_underline=True)
        self.play(FadeIn(title_intro))

        introtext2 = TexText(r"如图的函数图像，在$x>0$时显然上升得越来越快.",color=BLACK)
        introtext3 = Text(text="那么我们怎么衡量这个变化快慢呢？",font="simsun",color=BLACK)
        introtext4 = Text(text="导数，反映了一个函数在某一点处的变化率.",font="simsun",t2c={"导数": RED,"，反映了一个函数在某一点处的变化率.":BLACK})
        introtext5 = TexText(r"导数可记为$y'$.\\ 它的几何意义就是某一点处的切线斜率\\(即直线$y=kx+b$的$k$值).",color=BLACK)

        df, num = dflabel = VGroup(
            TexText("切线斜率$k_l=y'=$",color=BLACK),
            DecimalNumber(1.4,num_decimal_places=2,color=BLACK,show_ellipsis=True)
        )
        num.set_color(BLACK)
        dflabel.arrange(RIGHT)

        textgroup = VGroup(introtext2, introtext3, introtext4, introtext5, dflabel)
        textgroup.arrange(DOWN, buff=0.4)
        textgroup.shift(RIGHT*3)
        # textgroup.shift(UP)
        textgroup.scale(0.7)

        #坐标系解释
        axes0 = Axes((-1,4),(-2,4),width=8,height=6,axis_config={"stroke_width":2,"stroke_color":BLACK, "include_tip":True})
        func_graph0 = axes0.get_graph(lambda x: x*x,x_range=[0,2.5], color=BLACK)
        f_group = VGroup(axes0,func_graph0)
        f_group.shift(LEFT*4)
        f_group.shift(DOWN)
        f_group.scale(0.6)
        dot_P_0 = Dot(color=RED)
        dot_P_L = Tex("\emph{P}",color=RED)
        dot_P_0.move_to(axes0.i2gp(0.7,func_graph0))
        dot_P_L.next_to(dot_P_0)

        self.play(Write(introtext2),ShowCreation(axes0), ShowCreation(func_graph0))
        self.wait(2)
        self.play(Write(introtext3))
        self.wait(2)
        self.play(Write(introtext4))
        self.wait(2)
        self.play(Write(introtext5),run_time=4)
        self.play(FadeIn(dot_P_0), FadeIn(dot_P_L))
        self.play(FadeIn(dflabel))
        
        t = 0.7
        tline = axes0.get_graph(lambda x:2*t*(x-t)+t*t,x_range=[-1,4],color=BLACK)
        self.play(Write(tline))
        
        #用于播放动态切线动画
        flag = True
        for t in np.linspace(0.70,2.12,150):
            if flag:
                tline0 = axes0.get_graph(lambda x:2*t*(x-t)+t*t,x_range=[-1,4],color=BLACK)
                self.play(ReplacementTransform(tline,tline0),dot_P_0.animate.move_to(axes0.i2gp(t,func_graph0)),dot_P_L.animate.next_to(dot_P_0),run_time=0.00015)
                flag = False
            else:
                tline = axes0.get_graph(lambda x:2*t*(x-t)+t*t,x_range=[-1,4],color=BLACK)
                self.play(ReplacementTransform(tline0,tline),dot_P_0.animate.move_to(axes0.i2gp(t,func_graph0)),dot_P_L.animate.next_to(dot_P_0),run_time=0.00015)
                flag = True
            num.set_value(2*t)
            num.set_color(BLACK)

        self.wait(3)
        self.play(FadeOut(textgroup))
        self.wait(1)
        
        defineText1, defineText2, defineText3, defineText4 = defineTextGroup = VGroup(
            TexText(r"对于二次函数$y=ax^2+bx+c$，有",color=BLACK),
            TexText(r"$y'=2ax+b.$",color=BLUE),
            TexText(r"例如，函数$y=x^2+x$在$x=0.5$时的切线斜率即为",color=BLACK),
            TexText(r"$k=y'=2\times 1\times 0.5 + 1=2.$",color=BLUE)
        )
                
        defineTextGroup.arrange(DOWN, buff=0.4)
        defineTextGroup.shift(RIGHT*3)
        defineTextGroup.scale(0.7)

        self.play(Write(defineText1))
        self.play(Write(defineText2))
        self.wait(1.5)
        self.play(Write(defineText3))
        self.play(Write(defineText4))
        self.wait(3)

        self.play(FadeOut(defineTextGroup),FadeOut(f_group),FadeOut(tline),FadeOut(dot_P_0),FadeOut(dot_P_L),FadeOut(tline0),FadeOut(title_intro))
            
        #题目
        title_2 = Title("2019武汉中考题",color=BLACK,include_underline=True)
        self.play(FadeIn(title_2))

        axes = Axes((-4,4),(-2,4),width=8,height=6,axis_config={"stroke_width":2,"stroke_color":BLACK, "include_tip":True})
        func_graph = axes.get_graph(lambda x: x*x,x_range=[-2,2], color=BLACK)
        func_label = axes.get_graph_label(func_graph, "y=x^2")
        func_label.to_corner(UL)

        dot_M_0 = Dot(color=RED)
        dot_M_L = Tex("\emph{M}",color=RED)
        dot_M_0.move_to(axes.i2gp(1.2,func_graph))
        dot_M_L.next_to(dot_M_0)
        dot_M = VGroup(dot_M_0, dot_M_L)

        dot_N_0 = Dot(color=RED)
        dot_N_L = Tex("\emph{N}",color=RED)
        dot_N_0.move_to(axes.i2gp(-0.8,func_graph))
        dot_N_L.next_to(dot_N_0,LEFT)
        dot_N = VGroup(dot_N_0, dot_N_L)

        dot_E_0 = Dot(color=RED,point=axes.c2p(0.2,-0.96))
        dot_E_L = Tex("\emph{E}",color=RED)
        dot_E_L.next_to(dot_E_0,DOWN)
        dot_E = VGroup(dot_E_0, dot_E_L)

        line_MN = Line(start=dot_N_0,end=dot_M_0,color=RED)
        line_ME = Line(start=dot_M_0,end=dot_E_0,color=RED)
        line_NE = Line(start=dot_N_0,end=dot_E_0,color=RED)
        

        graphs = VGroup(dot_M, dot_N, dot_E ,line_MN, line_ME, line_NE, func_graph, axes)

        self.play(FadeIn(axes))
        self.play(ShowCreation(func_graph),FadeIn(func_label))
        self.play(ShowCreation(dot_M),ShowCreation(dot_N),ShowCreation(dot_E),ShowCreation(line_MN),ShowCreation(line_ME),ShowCreation(line_NE))
        self.play(graphs.animate.scale(0.7),FadeOut(func_label))
        self.play(graphs.animate.shift(LEFT*4))


        problem = TexText(r"""如图，$\triangle MNE$ 的顶点$M$,$N$在抛物线$y=x^2$上，\\点$M$在点$N$右边，\\ 两条直线$ME$,$NE$与抛物线相切. \\
        若$\triangle MNE$的面积为2,\\ 设$M$,$N$两点的横坐标分别为$m$,$n$ ,\\ 求$m$与$n$的数量关系.""",color=BLACK,font_size=30)
        problem.shift(RIGHT*3)
        self.play(Write(problem),run_time=6)
        self.wait(4)
        self.play(FadeOut(problem))

        solve = TexText(r"""根据刚才的求导公式，容易知道\\$k_{ME}=2ax+b=2\times 1\times m + 0 =2m$，\\
        同理$k_{NE}=2n$.\\
        点斜式易写出$l_{ME}:y=2mx-m^2$，$l_{NE}:y=2nx-n^2$\\
        联立求得$E(\frac{m+n}{2},mn)$.""",color=BLACK,font_size=30)
        solve.shift(RIGHT*3)
        self.play(FadeIn(solve))
        self.wait(8)
        self.play(FadeOut(solve))

        solve1 = TexText(r"""利用铅垂法表示面积.\\
            容易求得$l_{MN}:y=(m+n)x-mn.$\\
            代入$x_E$得$F(\frac{m+n}{2},\frac{m^2+n^2}{2})$\\
            则$EF=y_F-y_E=\frac{1}{2}(m-n)^2$\\
            $S=\frac{1}{2} \times (m-n) \times \frac{1}{2}(m-n)^2=2$\\
            从而$m-n=2$.""",color=BLACK,font_size=30)
        solve1.shift(RIGHT*3)

        dot_F_0 = Dot(color=RED,point=axes.c2p(0.2,1.04))
        dot_F_L = Tex("\emph{F}",color=RED)
        dot_F_L.next_to(dot_F_0)
        dot_F = VGroup(dot_F_0, dot_F_L)
        line_EF = Line(start=dot_E_0,end=dot_F_0,color=RED)
        self.play(ShowCreation(dot_F),ShowCreation(line_EF),FadeIn(solve1))
        self.wait(8)










if __name__ == "__main__":
    system("manimgl {} Derivative -w -c white".format(__file__))
