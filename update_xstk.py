import re

with open("d:\\KTHP 2026\\ECO152-leduc\\congthuc.html", "r", encoding="utf-8") as f:
    content = f.read()

html_content = r"""        <!-- XSTK CONTENT -->
        <div id="content-xstk" style="display: none;">
            <nav class="nav-tabs">
                <button class="nav-tab active" data-subject="xstk" data-section="section1">🎲 Chương 1 & 2</button>
                <button class="nav-tab" data-subject="xstk" data-section="section2">📊 Chương 3: Phân Phối</button>
                <button class="nav-tab" data-subject="xstk" data-section="section3">📈 Chương 4: Ước Lượng</button>
                <button class="nav-tab" data-subject="xstk" data-section="section4">💡 Tips Bấm Máy</button>
            </nav>

            <div id="xstk-section1" class="section xstk-section active">
                <h3>CHƯƠNG 1: DỮ LIỆU & THỐNG KÊ MÔ TẢ (Ăn điểm trắc nghiệm dễ)</h3>
                
                <div class="card">
                    <h4>1. Phân loại biến và Thang đo</h4>
                    <ul>
                        <li><strong>Biến liên tục:</strong> Có thể nhận giá trị lẻ, thập phân (VD: <em>Chiều cao, trọng lượng quả bí ngô...</em>).</li>
                        <li><strong>Biến rời rạc:</strong> Chỉ nhận giá trị nguyên (VD: <em>Số khách chờ xe buýt, số học sinh...</em>).</li>
                        <li><strong>Các loại thang đo (Có 4 loại):</strong>
                            <ul>
                                <li><em>Danh nghĩa (Nominal):</em> Chỉ để gọi tên, phân loại (VD: <em>Màu tóc, giới tính, dân tộc</em>).</li>
                                <li><em>Thứ hạng (Ordinal):</em> Có sắp xếp cao thấp (VD: <em>Giỏi, Khá, Trung bình</em>).</li>
                                <li><em>Khoảng (Interval):</em> Không có số 0 tuyệt đối (VD: <em>Nhiệt độ C</em>).</li>
                                <li><em>Tỷ lệ (Ratio):</em> Có số 0 tuyệt đối, so sánh gấp mấy lần (VD: <em>Chiều cao, Cân nặng, Thu nhập</em>).</li>
                            </ul>
                        </li>
                    </ul>
                </div>

                <div class="card">
                    <h4>2. Các đặc trưng của dãy số liệu</h4>
                    <p><em>(VD dãy số: 3, 4, 2, 3, 4, 1, 5, 7)</em></p>
                    <ul>
                        <li><strong>Kích thước mẫu (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math>):</strong> Tổng số phần tử trong dãy (Dãy trên <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi><mo>=</mo><mn>8</mn></mrow><annotation encoding="application/x-tex">n = 8</annotation></semantics></math>).</li>
                        <li><strong>Trung bình (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><mi>x</mi><mo>ˉ</mo></mover></mrow><annotation encoding="application/x-tex">\bar{x}</annotation></semantics></math>):</strong> Tổng các số chia cho <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math>.</li>
                        <li><strong>Mode (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>M</mi><mi>o</mi></msub></mrow><annotation encoding="application/x-tex">M_o</annotation></semantics></math>):</strong> Giá trị xuất hiện <strong>NHIỀU NHẤT</strong>. <em>(Có thể có nhiều Mode, VD dãy trên Mode là 3 và 4)</em>.</li>
                        <li><strong>Trung vị (Median - <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>M</mi><mi>e</mi></msub></mrow><annotation encoding="application/x-tex">M_e</annotation></semantics></math>):</strong> Giá trị đứng GIỮA dãy số <strong>SAU KHI ĐÃ SẮP XẾP TỪ BÉ ĐẾN LỚN</strong>.
                            <div class="tip"><em>Mẹo:</em> Đề cho: 10, 3, 7, 8, 9, 6, 7, 2 → Xếp lại: 2, 3, 6, <strong>7, 7</strong>, 8, 9, 10. Trung vị là trung bình cộng của 2 số ở giữa: <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mn>7</mn><mo>+</mo><mn>7</mn><mo stretchy="false">)</mo><mi mathvariant="normal">/</mi><mn>2</mn><mo>=</mo><mn>7</mn></mrow><annotation encoding="application/x-tex">(7+7)/2 = 7</annotation></semantics></math>.</div>
                        </li>
                        <li><strong>Khoảng biến thiên:</strong> = Giá trị MAX - Giá trị MIN. <em>(VD: 10 - 1 = 9)</em>.</li>
                        <li><strong>Phương sai (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mi>s</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">s^2</annotation></semantics></math> / <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>V</mi><mi>a</mi><mi>r</mi></mrow><annotation encoding="application/x-tex">Var</annotation></semantics></math>) & Độ lệch chuẩn (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math> / <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>σ</mi></mrow><annotation encoding="application/x-tex">\sigma</annotation></semantics></math>):</strong> 
                            <div class="note">Nhớ quy tắc: <em>Độ lệch chuẩn bằng Căn bậc 2 của Phương sai</em>. (Ví dụ: Đề cho Phương sai = 64 → Độ lệch chuẩn = 8).</div>
                        </li>
                    </ul>
                </div>

                <h3>CHƯƠNG 2: LÝ THUYẾT XÁC SUẤT CƠ BẢN</h3>
                <div class="card">
                    <p><em>Luôn nhớ: Xác suất của một biến cố A luôn nằm trong khoảng <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0</mn><mo>≤</mo><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo><mo>≤</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">0 \le P(A) \le 1</annotation></semantics></math>.</em></p>
                    <ul>
                        <li><strong>Biến cố đối (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><mi>A</mi><mo>ˉ</mo></mover></mrow><annotation encoding="application/x-tex">\bar{A}</annotation></semantics></math>):</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mover accent="true"><mi>A</mi><mo>ˉ</mo></mover><mo stretchy="false">)</mo><mo>=</mo><mn>1</mn><mo>−</mo><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(\bar{A}) = 1 - P(A)</annotation></semantics></math>. (VD: Đề cho <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo><mo>=</mo><mn>0.75</mn><mo>→</mo><mi>P</mi><mo stretchy="false">(</mo><mover accent="true"><mi>B</mi><mo>ˉ</mo></mover><mo stretchy="false">)</mo><mo>=</mo><mn>1</mn><mo>−</mo><mn>0.75</mn><mo>=</mo><mn>0.25</mn></mrow><annotation encoding="application/x-tex">P(B) = 0.75 \rightarrow P(\bar{B}) = 1 - 0.75 = 0.25</annotation></semantics></math>).</li>
                        <li><strong>Công thức CỘNG:</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A + B)</annotation></semantics></math> hoặc <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo>∪</mo><mi>B</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A \cup B)</annotation></semantics></math>
                            <ul>
                                <li>Trường hợp chung: <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo stretchy="false">)</mo><mo>=</mo><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo><mo>+</mo><mi>P</mi><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo><mo>−</mo><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mi mathvariant="normal">.</mi><mi>B</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A+B) = P(A) + P(B) - P(A.B)</annotation></semantics></math></li>
                                <li>Nếu A và B <strong>xung khắc</strong> (không thể cùng xảy ra): <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mi mathvariant="normal">.</mi><mi>B</mi><mo stretchy="false">)</mo><mo>=</mo><mn>0</mn><mo>→</mo><mi mathvariant="bold">P</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">A</mi><mo mathvariant="bold">+</mo><mi mathvariant="bold">B</mi><mo mathvariant="bold" stretchy="false">)</mo><mo mathvariant="bold">=</mo><mi mathvariant="bold">P</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">A</mi><mo mathvariant="bold" stretchy="false">)</mo><mo mathvariant="bold">+</mo><mi mathvariant="bold">P</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">B</mi><mo mathvariant="bold" stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A.B) = 0 \rightarrow \mathbf{P(A+B) = P(A) + P(B)}</annotation></semantics></math>.</li>
                            </ul>
                        </li>
                        <li><strong>Công thức NHÂN:</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mi mathvariant="normal">.</mi><mi>B</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A.B)</annotation></semantics></math> hoặc <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo>∩</mo><mi>B</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A \cap B)</annotation></semantics></math>
                            <ul>
                                <li>Trường hợp chung: <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mi mathvariant="normal">.</mi><mi>B</mi><mo stretchy="false">)</mo><mo>=</mo><mi>P</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo><mo>×</mo><mi>P</mi><mo stretchy="false">(</mo><mi>B</mi><mi mathvariant="normal">∣</mi><mi>A</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(A.B) = P(A) \times P(B|A)</annotation></semantics></math></li>
                                <li>Nếu A và B <strong>độc lập</strong> (thằng này xảy ra không ảnh hưởng tới thằng kia): <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="bold">P</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">A</mi><mi mathvariant="bold">.</mi><mi mathvariant="bold">B</mi><mo mathvariant="bold" stretchy="false">)</mo><mo mathvariant="bold">=</mo><mi mathvariant="bold">P</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">A</mi><mo mathvariant="bold" stretchy="false">)</mo><mo mathvariant="bold">×</mo><mi mathvariant="bold">P</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">B</mi><mo mathvariant="bold" stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">\mathbf{P(A.B) = P(A) \times P(B)}</annotation></semantics></math>. <br><em>(Câu này xuất hiện 100% ở cả Trắc nghiệm lẫn Tự luận ngắn).</em></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>

            <div id="xstk-section2" class="section xstk-section">
                <h3>CHƯƠNG 3: CÁC QUY LUẬT PHÂN PHỐI XÁC SUẤT (Trọng tâm)</h3>
                
                <div class="card">
                    <h4>1. Phân phối Nhị thức - Binomial <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>B</mi><mo stretchy="false">(</mo><mi>n</mi><mo separator="true">,</mo><mi>p</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">B(n, p)</annotation></semantics></math></h4>
                    <p><em>Dùng khi phép thử chỉ có 2 kết quả (Thành công/Thất bại), lặp lại n lần.</em></p>
                    <ul>
                        <li><strong>Công thức tính XS:</strong> 
                            <div class="formula-box"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>X</mi><mo>=</mo><mi>k</mi><mo stretchy="false">)</mo><mo>=</mo><msubsup><mi>C</mi><mi>n</mi><mi>k</mi></msubsup><mo>⋅</mo><msup><mi>p</mi><mi>k</mi></msup><mo>⋅</mo><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mi>p</mi><msup><mo stretchy="false">)</mo><mrow><mi>n</mi><mo>−</mo><mi>k</mi></mrow></msup></mrow><annotation encoding="application/x-tex">P(X = k) = C_n^k \cdot p^k \cdot (1-p)^{n-k}</annotation></semantics></math></div>
                            <div class="tip"><em>(Đề hỏi: Cho <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>X</mi><mo>∼</mo><mi>B</mi><mo stretchy="false">(</mo><mn>4</mn><mo separator="true">,</mo><mn>0.2</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">X \sim B(4, 0.2)</annotation></semantics></math>. Tìm <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>X</mi><mo>=</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(X=0)</annotation></semantics></math> → Bấm máy: <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>4</mn><mi>C</mi><mn>0</mn><mo>⋅</mo><mo stretchy="false">(</mo><mn>0.2</mn><msup><mo stretchy="false">)</mo><mn>0</mn></msup><mo>⋅</mo><mo stretchy="false">(</mo><mn>0.8</mn><msup><mo stretchy="false">)</mo><mn>4</mn></msup><mo>=</mo><mn>0.4096</mn></mrow><annotation encoding="application/x-tex">4C0 \cdot (0.2)^0 \cdot (0.8)^4 = 0.4096</annotation></semantics></math>).</em></div>
                        </li>
                        <li><strong>Kỳ vọng (Trung bình):</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="bold">E</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">X</mi><mo mathvariant="bold" stretchy="false">)</mo><mo mathvariant="bold">=</mo><mi mathvariant="bold">n</mi><mo mathvariant="bold">⋅</mo><mi mathvariant="bold">p</mi></mrow><annotation encoding="application/x-tex">\mathbf{E(X) = n \cdot p}</annotation></semantics></math></li>
                        <li><strong>Phương sai:</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="bold">V</mi><mi mathvariant="bold">a</mi><mi mathvariant="bold">r</mi><mo mathvariant="bold" stretchy="false">(</mo><mi mathvariant="bold">X</mi><mo mathvariant="bold" stretchy="false">)</mo><mo mathvariant="bold">=</mo><mi mathvariant="bold">n</mi><mo mathvariant="bold">⋅</mo><mi mathvariant="bold">p</mi><mo mathvariant="bold">⋅</mo><mo mathvariant="bold" stretchy="false">(</mo><mn mathvariant="bold">1</mn><mo mathvariant="bold">−</mo><mi mathvariant="bold">p</mi><mo mathvariant="bold" stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">\mathbf{Var(X) = n \cdot p \cdot (1-p)}</annotation></semantics></math>
                            <div class="note"><em>(Đề hỏi: <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi><mo>=</mo><mn>60</mn><mo separator="true">,</mo><mi>p</mi><mo>=</mo><mn>0.3</mn></mrow><annotation encoding="application/x-tex">n=60, p=0.3</annotation></semantics></math> → <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>E</mi><mo stretchy="false">(</mo><mi>X</mi><mo stretchy="false">)</mo><mo>=</mo><mn>60</mn><mo>⋅</mo><mn>0.3</mn><mo>=</mo><mn>18</mn></mrow><annotation encoding="application/x-tex">E(X) = 60 \cdot 0.3 = 18</annotation></semantics></math>; <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>V</mi><mi>a</mi><mi>r</mi><mo stretchy="false">(</mo><mi>X</mi><mo stretchy="false">)</mo><mo>=</mo><mn>60</mn><mo>⋅</mo><mn>0.3</mn><mo>⋅</mo><mn>0.7</mn><mo>=</mo><mn>12.6</mn></mrow><annotation encoding="application/x-tex">Var(X) = 60 \cdot 0.3 \cdot 0.7 = 12.6</annotation></semantics></math>).</em></div>
                        </li>
                    </ul>
                </div>

                <div class="card">
                    <h4>2. Phân phối Poisson <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>λ</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">P(\lambda)</annotation></semantics></math></h4>
                    <p><em>Dùng đếm số biến cố xảy ra trong một khoảng thời gian/không gian. (VD: Số cuộc gọi tới tổng đài trong 1 giờ).</em></p>
                    <ul>
                        <li><strong>Công thức:</strong> 
                            <div class="formula-box"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>X</mi><mo>=</mo><mi>k</mi><mo stretchy="false">)</mo><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>λ</mi></mrow></msup><mo>⋅</mo><msup><mi>λ</mi><mi>k</mi></msup></mrow><mrow><mi>k</mi><mo stretchy="false">!</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}</annotation></semantics></math></div>
                        </li>
                        <li><strong>Đặc điểm vàng:</strong> Kỳ vọng = Phương sai = <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>λ</mi></mrow><annotation encoding="application/x-tex">\lambda</annotation></semantics></math>.</li>
                    </ul>
                </div>

                <div class="card">
                    <h4>3. Phân phối Chuẩn - Normal <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi><mo stretchy="false">(</mo><mi>μ</mi><mo separator="true">,</mo><msup><mi>σ</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">N(\mu, \sigma^2)</annotation></semantics></math></h4>
                    <ul>
                        <li>Phân phối chuẩn tắc <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Z</mi><mo>∼</mo><mi>N</mi><mo stretchy="false">(</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">Z \sim N(0,1)</annotation></semantics></math> có Trung bình = 0, Độ lệch chuẩn = 1.</li>
                        <li><em>Câu học thuộc lòng:</em> Cho Z là chuẩn tắc, <strong><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo stretchy="false">(</mo><mi>Z</mi><mo>&lt;</mo><mn>1</mn><mo stretchy="false">)</mo><mo>=</mo><mn>0.8413</mn></mrow><annotation encoding="application/x-tex">P(Z &lt; 1) = 0.8413</annotation></semantics></math></strong> (Trong đề hay làm tròn là 0.841).</li>
                    </ul>
                </div>

                <div class="card">
                    <h4>4. Phân phối Siêu bội (Hypergeometric)</h4>
                    <ul>
                        <li><em>Mẹo nhận diện:</em> Các bài toán "Bốc ngẫu nhiên k vật từ 1 tập hợp N vật có sẵn (VD: chọn 10 xe trong 50 xe có 20 xe đỏ, chọn 4 người từ nhóm nam nữ...)". <strong>Đó chính là Siêu bội</strong>.</li>
                    </ul>
                </div>
            </div>

            <div id="xstk-section3" class="section xstk-section">
                <h3>CHƯƠNG 4: THỐNG KÊ SUY DIỄN & ƯỚC LƯỢNG (Bao trọn câu Tự luận 3 điểm)</h3>
                
                <div class="card">
                    <h4>1. Phương pháp lấy mẫu</h4>
                    <p>Có 4 phương pháp cơ bản (Ngẫu nhiên đơn giản, Hệ thống, Phân tầng, Theo chùm).</p>
                    <div class="tip"><em>Mẹo:</em> Cứ "chọn sản phẩm thứ 50 trên dây chuyền" → <strong>Mẫu hệ thống</strong>.</div>
                </div>

                <div class="card">
                    <h4>2. BÀI TOÁN TỰ LUẬN 3 ĐIỂM (Cứ áp khuôn này là 100% full điểm)</h4>
                    <div class="note"><strong>Ví dụ từ đề thi:</strong> Khảo sát mẫu 200 linh kiện (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi><mo>=</mo><mn>200</mn></mrow><annotation encoding="application/x-tex">n=200</annotation></semantics></math>), có 170 linh kiện đạt chất lượng (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi><mo>=</mo><mn>170</mn></mrow><annotation encoding="application/x-tex">k=170</annotation></semantics></math>). Độ tin cậy 95% (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>z</mi><mrow><mi>α</mi><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msub><mo>=</mo><mn>1.96</mn></mrow><annotation encoding="application/x-tex">z_{\alpha/2} = 1.96</annotation></semantics></math>).</div>
                    
                    <ul style="margin-top: 15px;">
                        <li><strong>Câu a (1 điểm): Tìm tỉ lệ mẫu.</strong>
                            <div class="formula-box">Công thức: <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><mi>p</mi><mo>^</mo></mover><mo>=</mo><mfrac><mi>k</mi><mi>n</mi></mfrac></mrow><annotation encoding="application/x-tex">\hat{p} = \frac{k}{n}</annotation></semantics></math></div>
                            <em>Giải:</em> Tỉ lệ linh kiện đạt chất lượng là <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><mi>p</mi><mo>^</mo></mover><mo>=</mo><mfrac><mn>170</mn><mn>200</mn></mfrac><mo>=</mo><mn>0.85</mn></mrow><annotation encoding="application/x-tex">\hat{p} = \frac{170}{200} = 0.85</annotation></semantics></math> (hoặc 85%).
                        </li>
                        <li style="margin-top: 15px;"><strong>Câu b (2 điểm): Ước lượng khoảng cho tỉ lệ tổng thể (Khoảng tin cậy).</strong>
                            <ul>
                                <li><em>Bước 1:</em> Tính Sai số biên (Độ chính xác của ước lượng):
                                    <div class="formula-box"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>ε</mi><mo>=</mo><msub><mi>z</mi><mrow><mi>α</mi><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msub><mo>×</mo><msqrt><mfrac><mrow><mover accent="true"><mi>p</mi><mo>^</mo></mover><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mover accent="true"><mi>p</mi><mo>^</mo></mover><mo stretchy="false">)</mo></mrow><mi>n</mi></mfrac></msqrt></mrow><annotation encoding="application/x-tex">\varepsilon = z_{\alpha/2} \times \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}</annotation></semantics></math></div>
                                    <div class="formula-box">→ <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>ε</mi><mo>=</mo><mn>1.96</mn><mo>×</mo><msqrt><mfrac><mrow><mn>0.85</mn><mo>×</mo><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mn>0.85</mn><mo stretchy="false">)</mo></mrow><mn>200</mn></mfrac></msqrt><mo>≈</mo><mn>0.049</mn></mrow><annotation encoding="application/x-tex">\varepsilon = 1.96 \times \sqrt{\frac{0.85 \times (1 - 0.85)}{200}} \approx 0.049</annotation></semantics></math></div>
                                </li>
                                <li><em>Bước 2:</em> Viết khoảng tin cậy:
                                    <div class="formula-box"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mover accent="true"><mi>p</mi><mo>^</mo></mover><mo>−</mo><mi>ε</mi><mo separator="true">;</mo><mover accent="true"><mi>p</mi><mo>^</mo></mover><mo>+</mo><mi>ε</mi><mo stretchy="false">)</mo><mo>=</mo><mo stretchy="false">(</mo><mn>0.85</mn><mo>−</mo><mn>0.049</mn><mo separator="true">;</mo><mn>0.85</mn><mo>+</mo><mn>0.049</mn><mo stretchy="false">)</mo><mo>=</mo><mo stretchy="false">(</mo><mn>0.801</mn><mo separator="true">;</mo><mn>0.899</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(\hat{p} - \varepsilon ; \hat{p} + \varepsilon) = (0.85 - 0.049 ; 0.85 + 0.049) = (0.801 ; 0.899)</annotation></semantics></math></div>
                                </li>
                            </ul>
                            <div class="tip"><em>(Lưu ý: Trong đáp án của GV là <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mn>0.78</mn><mo separator="true">,</mo><mn>0.92</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(0.78, 0.92)</annotation></semantics></math> có thể do sai số làm tròn hoặc trong bài giảng thầy cô cho dùng công thức làm tròn khác, nhưng cấu trúc chuẩn xác 100% trên thế giới là như trên).</em></div>
                        </li>
                    </ul>
                </div>
            </div>

            <div id="xstk-section4" class="section xstk-section">
                <h3>🚀 TIPS "BẤM MÁY TÍNH" ĐỂ LÀM TRẮC NGHIỆM THẦN TỐC</h3>
                
                <div class="card">
                    <p>Khi đi thi, đừng tính tay Độ lệch chuẩn hay Trung bình. Hãy dùng máy tính CASIO (Fx-580VN X hoặc Fx-570VN Plus):</p>
                    <ul>
                        <li><strong>Với máy 580VN X:</strong>
                            <ol>
                                <li>Ấn <code>MENU</code> → <code>6</code> (Thống kê) → <code>1</code> (1 biến).</li>
                                <li>Nhập các số liệu vào cột <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math>.</li>
                                <li>Ấn <code>OPTN</code> → <code>2</code> (Tính 1 biến).</li>
                                <li>Màn hình sẽ hiện toàn bộ: 
                                   <ul>
                                       <li><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><mi>x</mi><mo>ˉ</mo></mover></mrow><annotation encoding="application/x-tex">\bar{x}</annotation></semantics></math>: Giá trị trung bình.</li>
                                       <li><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>s</mi><mi>x</mi></msub></mrow><annotation encoding="application/x-tex">s_x</annotation></semantics></math>: Độ lệch chuẩn mẫu (dùng cái này).</li>
                                       <li><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>σ</mi><mi>x</mi></msub></mrow><annotation encoding="application/x-tex">\sigma_x</annotation></semantics></math>: Độ lệch chuẩn tổng thể.</li>
                                       <li><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>m</mi><mi>e</mi><mi>d</mi></mrow><annotation encoding="application/x-tex">med</annotation></semantics></math>: Trung vị.</li>
                                   </ul>
                                </li>
                            </ol>
                        </li>
                        <li><strong>Với các bài Tổ hợp (chọn đồ vật):</strong>
                            <ul>
                                <li>Ví dụ: Rút ngẫu nhiên 4 xe từ 7 chiếc Porsche và 12 chiếc BMW. Xác suất bốc 4 BMW?</li>
                                <li><em>Cách bấm:</em> <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mi>C</mi><mn>4</mn></mrow><mrow><mn>19</mn><mi>C</mi><mn>4</mn></mrow></mfrac><mo>≈</mo><mn>0.128</mn></mrow><annotation encoding="application/x-tex">P = \frac{12C4}{19C4} \approx 0.128</annotation></semantics></math> (Bấm phím <code>nCr</code> trên máy tính).</li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </div>\n\n        <button class="back-to-top" id="backToTop">↑</button>"""

def replace_match(match):
    return html_content

pattern = re.compile(r"        <!-- XSTK CONTENT -->\n        <div id=\"content-xstk\" style=\"display: none;\">.*?<button class=\"back-to-top\" id=\"backToTop\">↑</button>", re.DOTALL)
new_content = pattern.sub(replace_match, content)

with open("d:\\KTHP 2026\\ECO152-leduc\\congthuc.html", "w", encoding="utf-8") as f:
    f.write(new_content)
